
from django.contrib import admin
from django.urls import path
from  mygallery import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('login_user/', views.login_user, name='login_user'),  
    path('logout_user/', views.logout_user, name='logout_user'),  
    path('signup/', views.register, name='signup'),  
    path('add_photo/',views.add_photo, name='add_photo'),
    path('photo_details',views.details, name='photo_details'),
]



