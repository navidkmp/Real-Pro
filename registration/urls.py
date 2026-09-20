from django.urls import path
from . import views


app_name = 'registration'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('forget-pass', views.forget_pass, name='forget_pass'),
]