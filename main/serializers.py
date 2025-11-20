from rest_framework import serializers
from .models import Category, Post, Comment
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
      class Meta:
            model = Category
            fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
      class Meta:
            model = Comment
            fields = ['id','user','post','body','created',]


class PostSerializer(serializers.ModelSerializer):
      user = serializers.SlugRelatedField(read_only=True,slug_field='username')
      comments = CommentSerializer(many=True,read_only=True)
      class Meta:
            model = Post
            fields = ['id','user','category','title','content','image','published','comments','created']

class RegisterSerializer(serializers.ModelSerializer):
      password = serializers.CharField(write_only=True)
      class Meta:
            model = User
            fields = ['username','email','password']
      def create(self, validated_data):
          user = User.objects.create_user(username=validated_data['username'],email=validated_data.get('email',''),password=validated_data['password'])
          return user
