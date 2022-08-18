from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from .models import Comment

# Create your views here.
def addcomment(request):
    print("I am add");
def viewcomment(request):
    print("I am view")
