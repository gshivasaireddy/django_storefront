from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F,DecimalField
from django.db.models.aggregates import Count,Max,Min,Avg,Sum
from django.db.models.expressions import Value,F,Func,ExpressionWrapper
from django.db.models.functions import Concat
from store.models import Product,OrderItem,Order,Customer

def say_hello(request):
    # Annotating Objects: Expression Wrapper
    # Case-1: Without ExpressionWrapper->throws exception 
    # queryset=Product.objects.annotate(
    #     discounted_price=F('unit_price')*0.8
    # )

    # case-2: With ExpressionWrapper
    discounted_price=ExpressionWrapper(F('unit_price')*0.8,output_field=DecimalField())
    queryset=Product.objects.annotate(
        discounted_price=discounted_price
    )

    return render(request, 'hello.html', {'name': 'Mosh','result':list(queryset)},
    )
