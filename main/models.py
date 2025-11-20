from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
      name = models.CharField(max_length=100)
      def __str__(self):
          return self.name

class Post(models.Model):
      user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
      category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
      title = models.CharField(max_length=100)
      content = models.TextField()
      image = models.ImageField(upload_to='posts/', blank=True, null=True)
      published = models.BooleanField(default=True)
      created = models.DateTimeField(auto_now_add=True)
      def __str__(self):
          return self.title

class Comment(models.Model):
      post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      body = models.TextField()
      created = models.DateTimeField(auto_now_add=True)
      def __str__(self):
          return f'{self.user.username} - {self.post.title}'
# Create your models here.
