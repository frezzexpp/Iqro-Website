from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema_view, extend_schema

@extend_schema_view(
    post=extend_schema(summary="User Registration", tags=["Authentication"])
)
class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # Boshqa foydalanuvchilar uchun ochiq

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully", "user": serializer.data}, status=201)
        return Response(serializer.errors, status=400)


@extend_schema_view(
    post=extend_schema(summary="User Login", tags=["Authentication"])
)
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]  # Boshqa foydalanuvchilar uchun ochiq

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=200)
        return Response(serializer.errors, status=400)
