from rest_framework.routers import DefaultRouter
from .views import RegisterView, PostView, CommentView, CategoryView, ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts',PostView,basename='posts')
router.register(r'comments',CommentView,basename='comments')
router.register(r'category',CategoryView,basename='ctegory')

urlpatterns = [path('',include(router.urls)),
               path('profile/',ProfileView.as_view(),name='profile'),
               path('register/',RegisterView.as_view(),name='register'),
               path('token/',TokenObtainPairView.as_view(),name='token'),
               path('token-refresh/',TokenRefreshView.as_view(),name='token-refresh'),
]
