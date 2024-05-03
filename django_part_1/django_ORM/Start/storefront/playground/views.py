from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from store.models import Product,OrderItem,Order

def say_hello(request):
    # Selecting Related Objects: select_related(many to 1 or 1-1)
    # queryset=Product.objects.select_related('collection').all()

    # prefetch_related(many to many , one to many scenarios)
    # queryset=Product.objects.prefetch_related('promotions').select_related('collection').all()

    # Exercise: Get the last 5 orders with their Customer and items (including Product)
    queryset=Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    return render(request, 'hello.html', {'name': 'Mosh','orders':list(queryset)},
    )
