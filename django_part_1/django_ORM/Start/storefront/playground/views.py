from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from store.models import Product,OrderItem

def say_hello(request):
    # selecting fields to query by using values()-> returns key:value pairs
    queryset=Product.objects.values('id','title')

    # retriving related table columns as well
    queryset2=Product.objects.values('id','title','collection__title')

    # values_list() --> returns tuples
    queryset3=Product.objects.values_list('id','title','collection__title')

    # show all the products who has orders(OrderItem table contains all the order details) and sort by title
    queryset4=Product.objects.filter(id__in=OrderItem.objects.values('product__id').distinct()).order_by('title')

    return render(request, 'hello.html', {'name': 'Mosh','products':list(queryset4),'products3':list(queryset),'products2':list(queryset2),'products4':list(queryset)},
    )
