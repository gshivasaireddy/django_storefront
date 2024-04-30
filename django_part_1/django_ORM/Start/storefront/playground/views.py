from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from store.models import Product

def say_hello(request):
    # sorting 
    # ascending
    # queryset=Product.objects.order_by('title')
    # descending sort
    # order_by returns a query_set and it will evaluated lazy
    queryset=Product.objects.order_by('unit_price','-title')

    # earliest --> returns the first record itself by sorting in asc order --> similar to order_by('column')[0]
    product1=Product.objects.earliest('unit_price')

    # latest --> returns the first record itself by sorting in desc order --> similar to order_by('-column')[0]
    product2=Product.objects.latest('unit_price')

    return render(request, 'hello.html', {'name': 'Mosh','products':list(queryset),'product1':product1,'product2':product2})
