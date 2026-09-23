from django.shortcuts import render
from blog.models import Post

def home(request):
    latest_posts = Post.objects.all().order_by('-created_at')[:3]

    return render(request, 'home.html', {
        'latest_posts': latest_posts
    })