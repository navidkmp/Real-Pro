from django.shortcuts import render, get_object_or_404, redirect
from .models import Property, Owner


def property_list(request):
    properties = Property.objects.all()
    return render(request,'property/property.html',{'properties': properties})


def agent(request):
    owners = Owner.objects.all()
    return render(request,'property/agents.html',{'owners': owners}
    )


def property_detail(request, slug):
    if request.user.is_authenticated:
        property = get_object_or_404(Property,slug=slug)
        return render(request,'property/property_detail.html',{'property': property})
    else:
        return redirect('registration:signin')