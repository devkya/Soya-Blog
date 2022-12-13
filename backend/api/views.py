from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import *
from blog.models import Post, Category, Comment, PostImage
from rest_framework.response import Response


# Create your views here.
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializser
    
    def get_serializer_context(self):
        return {
            'request': None,
            'format': self.format_kwarg,
            'view': self
        }
        
# Post detail
class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializser


# 특정 게시글의 사진 불러오기
class PostDetailImageListAPIView(RetrieveAPIView):
    queryset = Post
    serializer_class = PostDetailImageSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        images = instance.postimage_set.all()
        
        data = {
            'thumbnail' : instance,
            'images' : images
        }
        serializer = self.get_serializer(instance=data)
        return Response(serializer.data)
    
    def get_serializer_context(self):
        return {
            'request': None,
            'format': self.format_kwarg,
            'view': self
        }
        

class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def list(self, request, *args, **kwargs):
        instance = self.get_queryset()
        pk = self.kwargs['pk']
        data = instance.filter(post=pk)

        serializer = self.get_serializer(instance=data, many=True)
        return Response(serializer.data)
    

# 여기서부터 하면 됨!  
class TotalImageListAPIView(ListAPIView):
    serializer_class = TotalImageSerializer
    
    def get(self, request, *args, **kwargs):
        thumbnail = Post.objects.values_list('thumbnail', flat=True)
        images = PostImage.objects.values_list('image', flat=True)
        
        data = {
           'thumbnail' : thumbnail,
           'images' : images
       }
        serializer = self.get_serializer(instance=data)
        return Response(serializer.data)