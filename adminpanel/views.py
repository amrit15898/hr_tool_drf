
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
# class AccessHrAndAdmin(BasePermission):
#     def has_permission(self, request, view):
#         now_user = request.user
#         # print(now_user.domain)
#         try:
#             user = User.objects.get(username=now_user)
#         except Exception as e:
#             print(e)
            
        
      
#         if user.domain.name == "HR" or user.is_staff or user.domain.name=="MD":
            

#             return True

        
            


class UserApi(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    

    def get(self, request):
        
        users = User.objects.filter(is_delete=False)
        serializer = UserSerializer(users, many=True)

        return Response({
            "status": 200,
            "message": "Get method called",
            "data": serializer.data
        })

    def post(self, request):
        data = request.data 
        user = request.user

        context = {
            "user": user
        }


        
        serializer = UserSerializer(data = data, context = context)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data["username"])
            refresh = RefreshToken.for_user(user)

            return Response({
                "status": 200, 
                "data": "data saved",
                "refresh": str(refresh),
                "access": str(refresh.access_token)

            })

        return Response({
            "message": "something went wrong",
            "error": serializer.errors

        })

    def delete(self, request):
        data = request.data
        print("delete requets call hoi")
        print(data)
        obj = User.objects.get(id=data.get('id'))
        print(obj.email)
    
        obj.is_delete = True
        obj.save()
        return Response({
            "message": "data successfully deleted"
        })

    def patch(self, request):
        data = request.data 
        try:

            obj = User.objects.get(id=data.get('id'))

        except User.DoesNotExist:
            return Response(
                {
                    "message": "id required"
                }
            )
        data = request.data 
        user = request.user

        context = {
            "user": user
        }


        
        
        serializer = UserSerializer(obj, data=data, partial=True, context = context)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True, 
                "message": "data successfully updated",
                "data": serializer.data

            })

        return Response({
            "status": False, 
            "message": "something went wrong",
            "errors": serializer.errors

        })
       
# class GetDomain(APIView):
#     def get(self, request):
#         objs = Domain.objects.all()
#         serializer = DomainSerializer(objs, many=True)

#         return Response({
#             "data": serializer.data

#         })

class DestroyUser(viewsets.ViewSet):
    def destroy(self, reuqest, pk):
        try:
            id = pk
            obj = User.objects.get(id=id)
            obj.delete()
            return Response({
                "message": "data deleted successfully"


            })

        except User.DoesNotExist:
            return Response({
                "message": "id not exit"
            })



        
