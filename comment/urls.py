from django.urls import include, path
from .import views

urlpatterns = [
    path('add/', views.addcomment, name='addcomment'),
    path('view/', views.viewcomment, name='viewcomment'),
]