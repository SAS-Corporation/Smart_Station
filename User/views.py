from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from User import serializers as user_serializers
from User import models as user_models
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone



# User registration view that handles user creation.
class UserRegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = user_serializers.UserRegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        app_name = "Adib Filling Station"
        return Response(
            {
                "message": (
                    f"Hi {user.first_name}, thank you for registering with {app_name}! "
                    f"An email with further instructions has been sent to **{user.email}**. "
                    f"Please check your inbox to continue."
                ),
                "user": {
                    "user_id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "phone": user.phone
                }
            },
            status=status.HTTP_201_CREATED
        )

class OTPVerificationView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = user_serializers.OTPVerificationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp_code = serializer.validated_data['otp_code']

            try:
                user = user_models.CustomUser.objects.get(email=email)
                otp_instance = user_models.EmailVerification.objects.get(user=user)

                if otp_instance.otp_code == otp_code and otp_instance.expires_at > timezone.now():
                    user.is_email_verified = True
                    user.save()
                    return Response({"message": "Email successfully verified."}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST)

            except user_models.CustomUser.DoesNotExist:
                return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)
            except user_models.EmailVerification.DoesNotExist:
                return Response({"message": "OTP not found for this user."}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View to handle user login.
class LoginView(APIView):
    permission_classes = [AllowAny]
   
    def post(self, request, *args, **kwargs):
        serializer = user_serializers.LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({
                "message": "Login successful.",
                "user": {
                    "user_id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                }
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

# View to handle user logout.
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Log out the user and clear the session
        logout(request)
        return Response({
            "message": "Logout successful."
        }, status=status.HTTP_200_OK)

