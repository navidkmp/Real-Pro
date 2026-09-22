from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        login(request, user)
        return redirect('home:home')

    return render(request, 'registration/signup.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect("home:home")

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            if remember_me:
                request.session.set_expiry(60 * 60 * 24 * 30)
            else:
                request.session.set_expiry(0)

            return redirect('home:home')

        return render(request, 'registration/signin.html', {
            'error': 'Invalid username or password.'
        })

    return render(request, 'registration/signin.html')




def forget_pass(request):
    return render(request, 'registration/password_reset/forget.html')



def logout_user(request):
    logout(request)
    return redirect('home:home')