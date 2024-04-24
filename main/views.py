from django.shortcuts import render
from django.conf import settings

api_key = settings.API_KEY

def dashboard(request):
    
    return render(request, "index.html")
