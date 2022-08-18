from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from post.models import Post

# Create your views here.

def index(request):
    allcategory = Category.objects.all()
    context = {
        'allcategory': allcategory,
    }
    return render(request, 'category/index.html',context)


def categorylist(request):
    catid=request.GET['id']
    #post = Post.objects.filter(category_id=catid)
    post = Post.objects.raw("SELECT * FROM post_post WHERE category_id="+catid)
    context = {
        'cat': post,
    }
    return render(request, 'category/listcategory.html',context)

