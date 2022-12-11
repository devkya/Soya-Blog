from django.urls import path, include
from blog.models import Post, Category, Comment, PostImage
from .views import *


app_name = 'api'
urlpatterns = [
    path('post/', PostListAPIView.as_view(), name='post-list'),
    path('image/', TotalImageListAPIView.as_view(), name='total-image'),
    
    path('post/<int:pk>/', PostListAPIView.as_view(), name='post-detail'),
    path('post/<int:pk>/image/', PostTotalImageListAPIView.as_view(), name='total-image'),
    path('post/<int:pk>/comment/', CommentListAPIView.as_view(), name='comment-list')
]
