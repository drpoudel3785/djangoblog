from django.urls import include, path
from .import views

urlpatterns = [
    path('allcategory/', views.index, name='allcategory'),
     path('list/', views.categorylist, name='categorylist'),
]