from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from blog import views

urlpatterns = [

    path('', views.home, name='home'),
    path('post-list/', views.post_list, name='post-list'),
    path('single-post/<id>/', views.single_post, name='single-post')

]
