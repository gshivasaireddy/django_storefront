from django.contrib import admin
from django.db.models.aggregates import Count
from . import models

# Register your models here.
# this class helps how we wanna view product on admin page
@admin.register(models.Product) # method-1
class ProductAdmin(admin.ModelAdmin):
  list_display=['title','unit_price','inventory_status','collection_title'] # selecting related obj -collection
  list_editable=['unit_price']
  list_per_page=10
  list_select_related=['collection']

  def collection_title(self,product):
    return product.collection.title  # related obj 

  @admin.display(ordering='inventory')
  def inventory_status(self,product):
    if product.inventory<10:
      return 'LOW'
    else:
      return 'OK'


# customization of Customer model
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
  list_display=['first_name','last_name','membership']
  list_editable=['membership']
  ordering=['first_name','last_name']
  list_per_page=10


# Let's setup the Order admin page
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
  list_display=['id','placed_at','customer']


# let's register our Collection app
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
  list_display=['title','products_count']

  @admin.display(ordering='products_count')
  def products_count(self,collection):
    return collection.products_count

  def get_queryset(self,request):
    return super().get_queryset(request).annotate(
      products_count=Count('product')
    )

