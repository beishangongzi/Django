from django.shortcuts import render
from myApp import models

# Create your views here.

def index(request):
    products = models.Product.objects.all()
    return render(request, 'index.html', locals())
