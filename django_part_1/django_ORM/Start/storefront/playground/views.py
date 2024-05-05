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
    # Querying Generic Relationships
    content_type=ContentType.objects.get_for_model(Product) #returns the row corresponding the content_type of Product class/model

    # filter for tagged item using content_type of Product
    queryset=TaggedItem.objects.select_related('tag').filter(
        content_type=content_type, # to map to Product
        object_id=1   # pass the product_id to get its tags
    ) # returns the list of tags for product_id=1

    return render(request, 'hello.html', {'name': 'Mosh','result':list(queryset)},
    )
