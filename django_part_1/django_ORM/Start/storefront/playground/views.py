from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from store.models import Product

def say_hello(request):
    # Limiting the results
    queryset=Product.objects.all()[:5]

    # limit 5 and offset 5
    queryset2=Product.objects.all()[5:10]

    

    return render(request, 'hello.html', {'name': 'Mosh','products':list(queryset),'products2':list(queryset2)})
