from django.shortcuts import render
from .models import Comment, Post, Category
from .serializers import CommentSerializer, PostSerializer, CategorySerializer, RegisterSerializer
from rest_framework import viewsets, filters, permissions, generics
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly

class RegisterView(generics.CreateAPIView):
      queryset = User.objects.all()
      serializer_class = RegisterSerializer
      permission_classes = [permissions.AllowAny]

class PostView(viewsets.ModelViewSet):
      serializer_class = PostSerializer
      permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
      queryset = Post.objects.all()

      def perform_create(self, serializer):
          serializer.save(user=self.request.user)

class CommentView(viewsets.ModelViewSet):
      queryset = Comment.objects.all()
      serializer_class = CommentSerializer
      permission_classes = [permissions.IsAuthenticatedOrReadOnly]
      def perform_create(self, serializer):
          serializer.save(user=self.request.user)

class CategoryView(viewsets.ModelViewSet):
      queryset = Category.objects.all()
      serializer_class = CategorySerializer
      permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfileView(APIView):
      permission_classes = [permissions.IsAuthenticated]
      def get(self, request):
          user = request.user
          return Response({'username':user.username,'email':user.email,'messages':f'Welcome Back {user.username}'})

# Create your views here.
