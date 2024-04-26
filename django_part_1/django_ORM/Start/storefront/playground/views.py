from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def say_hello(request):
    # filtering in detail
    # 
    #queryset =Product.objects.filter(unit_price__gt=20)
    # queryset =Product.objects.filter(collection__id__range=(1,2,3))
    #queryset =Product.objects.filter(last_update__year=2021)
    queryset = Product.objects.filter(description__isnull=True)
    
    

    return render(request, 'hello.html', {'name': 'Mosh','products':list(queryset)})
