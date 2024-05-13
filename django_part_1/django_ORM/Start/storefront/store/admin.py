from django.contrib import admin
from . import models

# this class helps how we wanna view product on admin page
@admin.register(models.Product) # method-1
class ProductAdmin(admin.ModelAdmin):
  list_display=['title','unit_price']

  # fields that can be editable
  list_editable=['unit_price']

  # list per page
  list_per_page=10

# let's register the products app
#admin.site.register(models.Product,ProductAdmin) # method-2

# customization of Customer model
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
  list_display=['first_name','last_name','membership']
  list_editable=['membership']
  ordering=['first_name','last_name']
  list_per_page=10
# Register your models here.
# let's register our Collection app
admin.site.register(models.Collection)

