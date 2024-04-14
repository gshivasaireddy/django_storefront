# in this module we are going to map the URL with our view functions

from django.urls import path
from . import views

# URL configuration
urlpatterns=[
  path('hello/',views.say_hello)
]