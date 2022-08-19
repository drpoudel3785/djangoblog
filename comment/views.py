from django.shortcuts import redirect, render
from django.db import connection
from django.http import HttpResponse
from .models import Comment
from django.contrib import messages
# Create your views here.
def addcomment(request):
        if request.method=='POST':
                cmt=request.POST['cmt']
                post_id=request.POST['post_id']
                user_id=request.POST['user_id']
                status=0
                cmts = Comment(cmt=cmt, status=status, post_id=post_id, user_id=user_id)
                cmts.save()
                messages.info(request, 'Comment added Successfully')
                return redirect("/post/details/?id="+post_id)    
        else:
                return redirect("/post/details/?id="+post_id) 
        
def viewcomment(request):
    print("I am view")

    


