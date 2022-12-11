from rest_framework import serializers
from blog.models import Post, Category, Comment, PostImage


class PostListSerializser(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'create_dt', 'origin_dt', 'like', 'thumbnail']
        
        
class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['thumbnail', 'create_dt', 'origin_dt']
        
    
class PostImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image', 'create_dt']
    
    
class PostDetailImageSerializer(serializers.Serializer):
    thumbnail = ThumbnailSerializer()
    images = PostImageListSerializer(many=True)
    
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'create_dt']
        
        
class TotalImageSerializer(serializers.Serializer):
    images = serializers.ListField(child=serializers.CharField())
    thumbnail = ThumbnailSerializer(many=True)