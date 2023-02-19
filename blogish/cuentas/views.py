from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import status 



def registerview(APIView):
    
    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'An error ocurred.'
                }, status = status.HTTP_400_BAD_REQUEST)
        
            serializer.save()

            return Response ({
                'data' : {},
                'message' : 'Your account has been successfully created'


            }, status = status.HTTP_201_CREATED)
    
        except Exception as a:
            return Response({
                'data' : {},
                'message' : 'An error ocurred.'
            }, status = status.HTTP_400_BAD_REQUEST)