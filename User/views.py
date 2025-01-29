from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from User import serializers as user_serializers
from User import models as user_models



# User registration view that handles user creation.
class UserRegisterView(generics.CreateAPIView):
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
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


