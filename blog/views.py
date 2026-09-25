from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from blog.models import Post


def blog(request):
        blog_posts = Post.objects.all()
        page_number = request.GET.get('page')
        paginator = Paginator(blog_posts, 6)
        objects_list = paginator.get_page(page_number)
        return render(request, "blog/blog.html", {"blog_posts": objects_list})



def blog_detail(request, slug):
        blog_post = get_object_or_404(Post, slug=slug)
        return render(request, "blog/blog_detail.html", {"blog_post": blog_post})




