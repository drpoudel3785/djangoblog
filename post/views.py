from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from comment.models import Comment

# Create your views here.
def index(request):
    allpost = Post.objects.all()
    context = {
        'allpost': allpost,
    }
    return render(request, 'post/index.html',context)
def details(request):
    postid=request.GET['id']
    #post = Post.objects.filter(id=postid)
    post = Post.objects.raw("SELECT * FROM post_post WHERE id="+postid)
    allcomment = Comment.objects.filter(post_id=postid, status=1).order_by('id').reverse()
    context = {
        'post': post,
        'allcomment':allcomment,
        'postid':postid
    }
    return render(request, 'post/details.html',context)

