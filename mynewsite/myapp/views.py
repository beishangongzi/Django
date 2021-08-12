from django.shortcuts import render
from django.http import Http404, HttpResponse
import random
from myapp.models import Product

# Create your views here.

def index(request):
    quotes = ["jaldcalpoc", "vlkaiap", "clkaf", "cjawpcca"]
    quote = random.choice(quotes)
    return render(request, 'index.html', locals())

def about(request):
    return render(request, 'about.html', locals())

def listing(request):
    products = Product.objects.all()
    return render(request, 'list.html', locals())

def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404("cannot find the num")
    return render(request, "disp.html", locals())
