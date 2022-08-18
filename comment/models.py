from site import USER_BASE
from tkinter import CASCADE
from django.db import models
from audioop import reverse
from django.contrib.auth.models import User
from django.conf import settings
from post.models import Post
# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True, null=True)
    post = models.ForeignKey(Post, verbose_name="postid", on_delete=models.SET_NULL, null=True)
    cmt = models.TextField (null=True)
    status = models.BooleanField(null=True) 
    createdate = models.DateField( auto_now=True)
    updatedate = models.DateField( auto_now=True)
    def __str__(self):
        return self.cmt
        
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])