from django.shortcuts import render

# Create your views here.
from urllib import response
from django.contrib.auth.models import User
from rest_framework import exceptions



from requests import request



from .serializer import UserRegistrationSerializer,UserLoginSerializer,UserListSerializer
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status,generics
from rest_framework.views import APIView
from django.http import JsonResponse

from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from rest_framework import viewsets
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.models import User



# user registration 
from rest_framework.response import Response
from rest_framework.decorators import api_view



from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model

from .serializer import UserSerializer









# Registration

class UserRegistrationView(APIView):


    def post(self, request):

        data = request.data
        serializer = UserRegistrationSerializer(data=data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()


            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'email': serializer.data["email"]
            }

            return Response(response)

        else:
            return JsonResponse({"message":"email/username already exists"})










# Login

class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],

                }
            }

            return Response(response, status=status_code)





# User Account

class UserAccountView(generics.RetrieveAPIView,generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user








#---------------------------------------logout ---------------------------------------


class LogoutView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return JsonResponse({"message":"logout"},status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return JsonResponse({"message":"invalid token"},status=status.HTTP_400_BAD_REQUEST)










#---------------------------------------logout end -------------------------------------







#---------------------- user list view ------------------------


class UserListView(viewsets.ModelViewSet):

    queryset = User.objects.all()

    serializer_class = UserListSerializer

    def list(self, request):
        queryset = User.objects.filter(id = self.request.user.id)
        # queryset = EventlikeModel.objects.filter()

        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # not permitted check
        if instance.id != self.request.user.id:
            print(instance.id)
            print(self.request.user)
            raise exceptions.PermissionDenied()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



#-----------------------user list view end --------------------


