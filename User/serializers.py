from rest_framework import serializers
from User import models as user_models
from django.contrib.auth.password_validation import validate_password


# Serializer to handle user registration with email as the username.
class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = user_models.CustomUser
        fields = ['email', 'first_name', 'last_name', 'phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create the user with email as the username
        user = user_models.CustomUser.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data.get('phone', ''),
        )
        return user
