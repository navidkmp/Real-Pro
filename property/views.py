from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Property, Owner, Agent


def property_list(request):
    properties = Property.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(properties, 6)
    objects_list = paginator.get_page(page_number)
    return render(request,'property/property.html',{'properties': objects_list})

def agent(request):
    agents = Agent.objects.all()
    return render(request,'property/agents.html',{'agents': agents})

def property_detail(request, slug):
    if request.user.is_authenticated:
        property = get_object_or_404(Property,slug=slug)
        return render(request,'property/property_detail.html',{'property': property})
    else:
        return redirect('registration:signin')