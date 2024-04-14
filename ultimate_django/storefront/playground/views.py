from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# A view functions take a request and returns a response
# request -> response
# It is a request handler.
# In some frameworks it is called action , in django it is called view. Dont be confused with Template.

def say_hello(request):
  return render(request,'hello.html',{'name':'SSR'})

