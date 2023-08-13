from django.shortcuts import render
from rest_framework import generics, permissions,viewsets,pagination
from rest_framework.response import Response

from .models import ServiceRequest
from .serializer import ServiceRequestSerializer
from .permission import IsobjectUser,IsAuthenticatedAndOwner
from .pagination import service_paginate
from datetime import timezone
# Create your views here.










class ServiceRequestView(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = (permissions.IsAuthenticated,)

    pagination_class = service_paginate


    def get_queryset(self):
        
        return ServiceRequest.objects.filter(customer=self.request.user)








class ServiceRequestUpdateStatusView(generics.UpdateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        instance = serializer.save()
        new_status = self.request.data.get('status', None)
        
        if new_status and new_status in [choice[0] for choice in ServiceRequest.STATUS_CHOICES]:
            instance.status = new_status
            instance.resolved_at = timezone.now() if new_status == 'Completed' else None
            instance.save()