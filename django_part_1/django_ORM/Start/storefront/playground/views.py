from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F,DecimalField
from django.db.models.aggregates import Count,Max,Min,Avg,Sum
from django.db.models.expressions import Value,F,Func,ExpressionWrapper
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from tags.models import TaggedItem
from store.models import Product,OrderItem,Order,Customer,Collection

# @transaction.atomic() --> use it as decorator to makes the whole fn atomic
def say_hello(request):
    # ...

    # Transactions
    with transaction.atomic():
        order=Order()
        order.customer_id=1
        order.save()

        item=OrderItem()
        item.order=order
        item.product_id=-1 # product_id=-1 doesn't exist it throws integrity issue
        item.quantity=1
        item.unit_price=10
        item.save()

    return render(request, 'hello.html', {'name': 'Mosh'},
    )
