from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


#what users see
#/products -recall-> index
def index(request):
    products = Product.objects.all()
    return render(request, "templates.html",
                  {"products": products})


