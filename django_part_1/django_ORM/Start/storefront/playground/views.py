from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F,DecimalField
from django.db.models.aggregates import Count,Max,Min,Avg,Sum
from django.db.models.expressions import Value,F,Func,ExpressionWrapper
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
from store.models import Product,OrderItem,Order,Customer

def say_hello(request):
    # Queryset caching example
    queryset=Product.objects.all()
    queryset[0] # indexing queryset first
    list(queryset)
    

    return render(request, 'hello.html', {'name': 'Mosh'},
    )
