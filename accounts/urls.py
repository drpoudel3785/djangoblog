from django.urls import include, path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='lgt'),
    
    path('Import_csv/', views.Import_csv, name="Import_csv"),  
    path('export_users_csv/', views.export_users_csv,name="export_users_csv"),
]