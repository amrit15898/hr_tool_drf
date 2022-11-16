from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

# class DomainSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Domain 

#         fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    # domain = serializers.StringRelatedField(many=True, read_only = True)
    
    class Meta:
        model = User
        fields = ["id", "username", "phone", "email", "position","domain", "role" , "address",  "password"]

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

    def validate(self, data):
        # user = self.context.get("user")
        # print(user)
        # obj = User.objects.get(username=user)
    
       
  
        # if obj.role =="HR" and data["role"] == "MD":
        #     raise serializers.ValidationError("Hr not create md")


        email = User.objects.filter(email = data.get('email'))




        if email:
            raise serializers.ValidationError("email is already exits please try with diffrent email")
        

        phone = data.get('phone')
        phone_exits = User.objects.filter(phone=phone)

        if phone_exits:
            raise serializers.ValidationError("phone number already registerd try with another number")


        if data.get('phone'):
            if (len(phone)>10 or len(phone)<10):
                raise serializers.ValidationError("please enter 10 digit number ")

        return data 
