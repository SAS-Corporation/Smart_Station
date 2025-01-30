from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from User import serializers as user_serializers
from User import models as user_models
from rest_framework.permissions import AllowAny



# User registration view that handles user creation.
class UserRegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = user_models.CustomUser.objects.all()
    serializer_class = user_serializers.UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User successfully registered.",
                "user": {
                    "user_id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                }
            }, status=status.HTTP_201_CREATED)
        
        # Let the custom exception handler handle the error
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
     
