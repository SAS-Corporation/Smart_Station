from rest_framework import serializers
from User import models as user_models
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model



User = get_user_model()

# Serializer to handle user registration with email as the username.
class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['message']:
            raise serializers.ValidationError({"message": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)

        # Check if a user with the same email exists
        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({"message": "A user with this email already exists."})

        # Create the user with email as the username
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data.get('phone', ''),
        )
        return user
    

# Serializer to handle user login with email and password.
class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        
        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        
        return {'user': user}

