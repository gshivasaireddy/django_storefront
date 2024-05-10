from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F,DecimalField
from django.db.models.aggregates import Count,Max,Min,Avg,Sum
from django.db.models.expressions import Value,F,Func,ExpressionWrapper
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from django.db import connection
from tags.models import TaggedItem
from store.models import Product,OrderItem,Order,Customer,Collection

def say_hello(request):
    # Executing RAW SQL Queries
    queryset=Product.objects.raw('SELECT * FROM store_product')
    
    # this raw sql query returns a queryset which is different from other querysets, this won't contain any methods which regular queryset contains

    # To deal with queries which don't involve django models
    # with connection.cursor() as cursor:
    #      cursor.execute()
    #      cursor.callproc('get_customers',[1,2,'a']) # execute the stored procedure which exists in DB


    return render(request, 'hello.html', {'name': 'Mosh','result':list(queryset)},
    )
