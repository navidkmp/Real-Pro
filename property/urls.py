from django.urls import path
from . import views

app_name = 'property'

urlpatterns = [
    path('agents', views.agent, name='agent'),
]