from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def say_hello(request):
    # case-1 : Query_sets looping
    # query_set = Product.objects.all()
    # for product in query_set:
    #     print(product)

    # case-2 : Query_sets converting to list
    # query_set = Product.objects.all()
    # result = list(query_set)

    # case-3 : specific value indexing or slicing the query_Set
    # query_set = Product.objects.all()
    # result =  query_set[3:5]

    # case-4 : return the count()
    query_set = Product.objects.count()
    print(query_set)




    return render(request, 'hello.html', {'name': 'Mosh'})
