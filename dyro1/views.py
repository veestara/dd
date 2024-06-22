from django.shortcuts import render
from .models import *


def home(request):
    if request.method == 'POST':
        name = request.POST.get('fullName')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, phone=phone, email=email, message=message)
        
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def sunpac_view(request):
    return render(request, "sunpac-view.html")

def test(request):
    return render(request, 'test.html')
