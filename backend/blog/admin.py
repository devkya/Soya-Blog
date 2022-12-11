from django.contrib import admin
from blog.models import *


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_dt', 'category']
    
    
@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post', 'create_dt', 'content']
    
        
@admin.register(PostImage)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post', 'image']
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']