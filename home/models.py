from django.db import models
from django.contrib.auth.models import User

class Details(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     age = models.IntegerField()
     gender=models.CharField(max_length=20)
     mobile=models.IntegerField()
     img = models.ImageField(upload_to='images/')


class Blog_Post(models.Model):
    details = models.ForeignKey(Details,on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    title = models.CharField(max_length=40)
    is_approved = models.BooleanField(default=False)

class Comment(models.Model):
     blog=models.ForeignKey(Blog_Post,on_delete=models.CASCADE)
     Comment=models.CharField(max_length=100)

class Reply(models.Model):
     Comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
     reply=models.CharField(max_length=100)

   