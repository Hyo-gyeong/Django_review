from django.shortcuts import render
from .models import Login
# Create your views here.

def login(request):
    return render(request, 'login.html')
