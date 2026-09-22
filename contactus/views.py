from django.shortcuts import render, redirect
from contactus.models import Contact




def contactus(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get('username')
            email = request.POST.get('email')
            Contact.objects.create(username=username, email=email)
        return render(request,'contactus/contactus.html')
    else:
        return redirect('registration:signin')

