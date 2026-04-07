from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import User
from .serializer import UserSerializer,RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN':
            return User.objects.all()
        # Normal user → only their own data
        return User.objects.filter(id=user.id)
    def retrieve(self, request, *args, **kwargs):
        user = self.request.user
        # Allow admin or self
        if user.role != 'ADMIN' and str(user.id) != kwargs.get('pk'):
            raise PermissionDenied("You can only view your own profile")

        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        user = self.request.user

        if user.role != 'ADMIN' and str(user.id) != kwargs.get('pk'):
            raise PermissionDenied("You can only update your own profile")

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.role != 'ADMIN':
            raise PermissionDenied("Only admin can delete users")

        return super().destroy(request, *args, **kwargs)
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Register successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "status": False,
            "message": "Registration failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)