from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Product

def say_hello(request):
    # complex lookups using Q-objects
    # ex-1: inventory<10 and price<20
    # queryset=Product.objects.filter(inventory__lt=10,unit_price__lt=20)
    # method-2
    # queryset=Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)

    # using Q-objects
    # Products: inventory <10 OR price<20
    # queryset=Product.objects.filter(Q(inventory__lt=10)|Q(unit_price__lt=20))
    queryset=Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))

    return render(request, 'hello.html', {'name': 'Mosh','products':list(queryset)})
