from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserProfileSerializer

from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.utils.encoding import force_str
from rest_framework.exceptions import ValidationError

class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            field, errors = list(e.detail.items())[0]
            message = force_str(errors[0])

            return Response({
                "success": False,
                "message": "Validation error.",
                "statusCode": status.HTTP_400_BAD_REQUEST,
                "errorDetails": {
                    "field": field,
                    "message": message
                }
            }, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        return Response({
            "success": True,
            "message": "Registration successful.",
            "statusCode": status.HTTP_201_CREATED,
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)




class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            errors = serializer.errors
            message = "Validation error occurred."
            if 'non_field_errors' in errors:
                message = "Validation failed."
                errors = errors['non_field_errors'][0]
            
            # If there are field errors (like missing fields), respond with 400 + detailed errors
            return Response({
                "success": False,
                "statusCode": 400,
                "message": message,
                "errorDetails": errors,
                "data": None
            }, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.validated_data.get('user')
        if not user:
            # Credentials are invalid, no user returned from serializer
            return Response({
                "success": False,
                "statusCode": 401,
                "message": "Invalid credentials",
                "data": None
            }, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response({
            "success": True,
            "statusCode": 200,
            "message": "Login successful",
            "data": {
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }
        }, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
