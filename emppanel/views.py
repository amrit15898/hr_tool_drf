from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from adminpanel.models import *
from adminpanel.serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class NormalUserApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        now_user = request.user
        
        obj = User.objects.get(username=now_user)
        serializer = UserSerializer(obj)
        return Response({
            "status": 200, 
            "data": serializer.data
        })

    def patch(self, request):
        
  
        data = request.data 
        user = request.user

        context = {
            "user": user
        }
        

        if not data.get('id'):
            return Response({
                "message": "id required"

            })
        try:
            obj = User.objects.get(id = data.get('id'))

        except Exception as e:
            return Response({
                "message": "id does not exit"
            })
        serializer = UserSerializer(obj, data = data, context=context, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "data successfully updted", 
                "data": serializer.data 
            })

        return Response({
            "message": "something went wrong",
            "errors": serializer.errors
        })
        
        