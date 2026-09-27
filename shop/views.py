from django.core.paginator import Paginator
from django.shortcuts import render


def shop(request):
    # blog_posts = .objects.all()
    # page_number = request.GET.get('page')
    # paginator = Paginator(blog_posts, 6)
    # objects_list = paginator.get_page(page_number)
    return render(request, 'shop/shop.html')
