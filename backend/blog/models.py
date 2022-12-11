from django.db import models
from datetime import date


     
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text='단어로 표기하세요.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True)
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    def image_path_rename(self, filename):
        today = date.today()
        filedate = today.strftime('%Y-%m-%d')
        return '{}/{}/{}'.format(filedate, self.title, filename)
    
    title = models.CharField('TITLE', max_length=50)
    content = models.TextField('content')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    create_dt = models.DateTimeField('CREATE_DT',auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE_DT', auto_now=True)
    origin_dt = models.DateField('ORIGIN_DT', blank=True, null=True, help_text="데이트 날짜 표기하세요.")
    like = models.PositiveSmallIntegerField('LIKE', default=0)
    thumbnail = models.ImageField('THUMBNAIL', upload_to=image_path_rename, unique=True)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    create_dt = models.DateTimeField(auto_now_add=True)
    content = models.TextField('CONTENT')
    

    
class PostImage(models.Model):
    def image_path_rename(self, filename):
        today = date.today()
        filedate = today.strftime('%Y-%m-%d')
        return '{}/{}/{}'.format(filedate, self.post, filename)
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField('IMAGE', upload_to=image_path_rename)
    create_dt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.image.url