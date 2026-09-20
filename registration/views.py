from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def signup(request):
    if request.user.is_authenticated == True:
        return redirect("home:home")
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'registration/signup.html', {
                'error': 'Passwords do not match.'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'registration/signup.html', {
                'error': 'Username already exists.'
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'registration/signup.html', {
                'error': 'Email already exists.'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        return redirect('registration:signin')

    return render(request, 'registration/signup.html')


def signin(request):
    if request.user.is_authenticated == True:
        return redirect("home:home")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('registration:signin')

        return render(request, 'registration/signin.html', {
            'error': 'Invalid username or password.'
        })

    return render(request, 'registration/signin.html')


def forget_pass(request):
    return render(request, 'registration/password_reset/forget.html')
