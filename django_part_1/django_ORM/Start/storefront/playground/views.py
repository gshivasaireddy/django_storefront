from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from store.models import Product

def say_hello(request):
    # F objects - used to compare fields and filter it
    # queryset=Product.objects.filter(inventory=F('unit_price'))
    queryset=Product.objects.filter(inventory=F('collection__id'))

    return render(request, 'hello.html', {'name': 'Mosh','products':list(queryset)})
