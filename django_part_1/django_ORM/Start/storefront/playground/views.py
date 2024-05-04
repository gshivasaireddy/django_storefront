from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from django.db.models.aggregates import Count,Max,Min,Avg,Sum
from django.db.models.expressions import Value,F,Func
from django.db.models.functions import Concat
from store.models import Product,OrderItem,Order,Customer

def say_hello(request):
    # Annotating Objects
    # queryset=Customer.objects.annotate(is_new=Value(True))

    # case-2 : Annotating with another field
    # queryset=Customer.objects.annotate(is_new=F('id')+1)

    # case-3: Annotating with Database Func Expressions
    # queryset=Customer.objects.annotate(
    #     # CONCAT first_name and last_name with a space in b/w
    #     full_name=Func(F('first_name'),Value(' '),F('last_name'),function='CONCAT')
    # )

    # Alternate way
    queryset=Customer.objects.annotate(full_name=Concat('first_name',Value(' '),'last_name'))

    return render(request, 'hello.html', {'name': 'Mosh','result':list(queryset)},
    )
