from rest_framework import serializers
from User import models as user_models
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status


# User = get_user_model()

# Serializer to handle user registration with email as the username.
class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = user_models.CustomUser
        fields = ['email', 'first_name', 'last_name', 'phone', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"message": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)

        if user_models.CustomUser.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({"message": "A user with this email already exists."})

        user = user_models.CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data.get('phone', ''),
        )

        # Generate OTP and send email
        otp_instance, created = user_models.EmailVerification.objects.get_or_create(user=user)
        otp_instance.generate_otp()

        app_name = "Adib Filling Station"

        # Create HTML email message
        html_message = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: 'Arial', sans-serif;
                    background-color: #fbe9d3;
                    margin: 0;
                    padding: 0;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background: linear-gradient(135deg, #fbe9d3, #e0a96d);
                    border-radius: 12px;
                    color: #5e3c16;
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                }}
                .email-header {{
                    padding: 20px;
                    text-align: center;
                    background-color: #e0a96d;
                    border-radius: 12px 12px 0 0;
                }}
                .email-header h1 {{
                    margin: 0;
                    font-size: 24px;
                    color: #ffffff;
                }}
                .email-body {{
                    padding: 25px;
                    background-color: #ffffff;
                    color: #5e3c16;
                    border-radius: 0 0 12px 12px;
                }}
                .email-body h2 {{
                    color: #c07f34;
                    font-size: 22px;
                    margin-bottom: 15px;
                }}
                .email-body p {{
                    font-size: 16px;
                    line-height: 1.6;
                    margin-bottom: 10px;
                }}
                .otp-code {{
                    display: inline-block;
                    padding: 12px 20px;
                    margin: 20px 0;
                    background-color: #c07f34;
                    color: white;
                    font-size: 22px;
                    font-weight: bold;
                    border-radius: 8px;
                    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.2);
                    letter-spacing: 2px;
                }}
                .email-footer {{
                    text-align: center;
                    padding: 12px;
                    font-size: 14px;
                    color: rgba(94, 60, 22, 0.8);
                    background: #fbe9d3;
                    border-radius: 0 0 12px 12px;
                }}
                .email-footer p {{
                    margin: 0;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="email-header">
                    <h1>{app_name}</h1>
                </div>
                <div class="email-body">
                    <h2>Hi {user.first_name},</h2>
                    <p>Welcome to <strong>{app_name}</strong>! To complete your registration, please verify your email using the OTP code below:</p>
                    <div class="otp-code">{otp_instance.otp_code}</div>
                    <p>This OTP is valid for 5 minutes. If you didn’t request this, you can safely ignore this email.</p>
                </div>
                <div class="email-footer">
                    <p>&copy; 2025 {app_name}. All Rights Reserved.</p>
                </div>
            </div>
        </body>
        </html>
        """

        # Send the email
        email = EmailMessage(
            subject=f"Welcome to {app_name} - Verify Your Email",
            body=html_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
        )
        email.content_subtype = "html"
        email.send()

        return user
    

# Serializer to handle user login with email and password.
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        
        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        
        if not user.is_email_verified:
            raise serializers.ValidationError("Email is not verified. Please check your inbox for the verification email.")
        
        return {'user': user}

class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp_code = serializers.CharField(required=True)

    