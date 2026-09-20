from django.shortcuts import render
from property.models import Agent


def agent(request):
    agents = Agent.objects.all()
    return render(request, 'property/agents.html',{'agents': agents})
