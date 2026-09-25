from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('posts',views.blog,name='blog'),
    path('posts/<slug:slug>',views.blog_detail,name='blog_detail'),
]