from site import USER_BASE
from tkinter import CASCADE
from django.db import models
from audioop import reverse
from django.contrib.auth.models import User
from django.conf import settings
from category.models import Category
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name="categoryid", on_delete=models.SET_NULL, null=True)
    title = models.TextField(max_length = 200, null=True)
    description = models.TextField(max_length = 200, null=True)
    keywords = models.TextField(max_length = 200, null=True)
    heading = models.TextField(max_length = 200, null=True)
    details = models.TextField (null=True)
    featureimage = models.ImageField(upload_to='static', null=True)
    status = models.BooleanField(null=True) 
    createdate = models.DateField( auto_now=True)
    updatedate = models.DateField( auto_now=True)
    def __str__(self):
        return self.heading
        
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])