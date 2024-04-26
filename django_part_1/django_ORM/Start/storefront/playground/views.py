from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def say_hello(request):

    # Retrieving methods such as get(),all(),filter()
    # try catch incase if the object value in store_product table doesn't exist
    # try:
    #     product=Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass

    # Alternate way is use filter() and retrieve first(), if it doesn't find , it returns None
    #product=Product.objects.filter(pk=0).first()

    # sometimes we want to check if the object exist/no
    product=Product.objects.filter(pk=0).exists()

    return render(request, 'hello.html', {'name': 'Mosh'})
