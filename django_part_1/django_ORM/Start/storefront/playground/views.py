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
    # Updating objects 
    # collection = Collection(pk=11)
    # collection.featured_product=None
    # collection.save()

    # collection=Collection.objects.get(pk=11)
    # collection.featured_product=None
    # collection.save()

    # update method
    Collection.objects.filter(pk=11).update(featured_product=None)

    return render(request, 'hello.html', {'name': 'Mosh'},
    )
