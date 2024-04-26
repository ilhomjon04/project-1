from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    rasm = models.ImageField(upload_to='user/', default='user_picture.png')

class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name




class News (models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    rasm = models.ImageField(upload_to = "rasm/", null = True, blank = True)
    author  = models.ForeignKey(User, on_delete = models.CASCADE)
    tur = models.ForeignKey(Category,on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add =True)
    views = models.PositiveBigIntegerField(default = 0)
    likes = models.ManyToManyField(User,related_name="likes")
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='like_1')
    

    def __str__(self):
        return self.title


class Comment (models.Model):
    izoh = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    news = models.ForeignKey(News, on_delete = models.CASCADE, related_name='comment')
    created = models.DateTimeField(auto_now_add = True)
    

    def __str__(self):
        return self.izoh




# Create your models here.
