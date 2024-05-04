from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from django.db.models.aggregates import Count,Max,Min,Avg,Sum
from django.db.models.expressions import Value,F
from store.models import Product,OrderItem,Order,Customer

def say_hello(request):
    # Annotating Objects
    # queryset=Customer.objects.annotate(is_new=Value(True))

    # case-2 : Annotating with another field
    queryset=Customer.objects.annotate(is_new=F('id')+1)

    return render(request, 'hello.html', {'name': 'Mosh','result':list(queryset)},
    )
