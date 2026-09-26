from django.urls import path
from . import views


app_name = 'property'

urlpatterns = [
    path('listing', views.property_list, name='property_list'),
    path('agents', views.agent, name='agent'),

    path(
        'property/<slug:slug>/',
        views.property_detail,
        name='property_detail'
    ),
]