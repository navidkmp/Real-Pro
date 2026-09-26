from django.shortcuts import render
from blog.models import Post
from property.models import Property

def home(request):
    latest_posts = Post.objects.all().order_by('-created_at')[:3]
    properties = Property.objects.all().order_by('-created_at')[:3]
    return render(request, 'home/home.html', {
        'latest_posts': latest_posts,
        'properties': properties
    })