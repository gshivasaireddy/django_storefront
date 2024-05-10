from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F,DecimalField
from django.db.models.aggregates import Count,Max,Min,Avg,Sum
from django.db.models.expressions import Value,F,Func,ExpressionWrapper
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
from store.models import Product,OrderItem,Order,Customer,Collection

def say_hello(request):
    # Creating objects 
    collection = Collection()
    # method-1 to set the value
    collection.title='Video Games'
    collection.featured_product_id=1
    
    # method-2 to set the value
    # collection.featured_product=Product(pk=1)
    
    
    # in both the cases the product with value=1 should exist
    # save() method inserts the data into DB
    collection.save()

    # alternate way of doing using create()
    #collection=Collection.objects.create(title='a',featured_product_id=1)
    

    return render(request, 'hello.html', {'name': 'Mosh'},
    )
