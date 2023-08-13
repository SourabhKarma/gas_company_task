

from rest_framework import generics, permissions,viewsets,pagination
from rest_framework.response import Response




class service_paginate(pagination.PageNumberPagination):

    page_size = 20
    page_size_query_param = 'page_size' 
    max_page_size = 100
    def get_paginated_response(self, data):

        return Response(data)



