
from rest_framework.response import Response
from rest_framework import generics, views
from .serializers import (
    UserRegisterSerializer,
    MyUserSerializer,
)
from .models import User
from rest_framework.permissions import IsAuthenticated


class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()


class MyProfileAPIView(generics.ListAPIView):
    serializer_class = MyUserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

