from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def validation(self, data):
        if User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError('Username already exists.')
        
        return data
    
    def create(self, validated_data):
        user = User.objects.create(first_name= validated_data['first_name'],
                                   last_name=validated_data['last_name'],
                                   username = validated_data['username'])
        user.set_password(validated_data['password'])

        return validated_data
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validation(self, data):
        
        if not User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError('Error : Account not found.')
        
        return data
    
    def authentication(self,data):

        user = authenticate(username = data['username'], password = data['password'])
        if not user :
            return {'message': 'Invalid login credentials', 'data': {}}
        return {'message': 'login ok', 'data': {}}
