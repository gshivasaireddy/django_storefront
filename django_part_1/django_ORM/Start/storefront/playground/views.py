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
    # Deleting objects
    collection=Collection(pk=11)
    collection.delete()

    # alternate way delete entire queryset
    Collection.objects.filter(id__gt=5).delete()

    return render(request, 'hello.html', {'name': 'Mosh'},
    )
