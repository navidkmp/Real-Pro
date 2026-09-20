from django.shortcuts import render
from contactus.models import Contact


def contactus(request):
    if request.method == "POST":
         username = request.POST.get('username')
         email = request.POST.get('email')
         Contact.objects.create(username=username, email=email)
    return render(request,'contactus/contactus.html')

