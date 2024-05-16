from django.contrib import admin
from django.db.models.aggregates import Count
from django.utils.html import format_html,urlencode
from django.urls import reverse
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
  list_display=['first_name','last_name','membership','orders']
  list_editable=['membership']
  ordering=['first_name','last_name']
  list_per_page=10

  @admin.display(ordering='orders_count')
  def orders(self,customer):
    url = (
      reverse('admin:store_order_changelist')
      + '?'
      + urlencode(
        {
          'customer__id':str(customer.id)
        }
      )
    )

    return format_html('<a href="{}">{} Orders</a>',url,customer.orders_count)

  def get_queryset(self,request):
    return super().get_queryset(request).annotate(
      orders_count=Count('order')
    )

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
    # reference --> reverse('admin:appname_modelname_page')
    # app:store,model:product,page:changelist
    url = (reverse('admin:store_product_changelist') # target url
    +'?'  # beginning of query
    + urlencode({
      'collection__id':str(collection.id)
    }))  # generate querystring parameter
    return format_html('<a href="{}">{}</a>',url,collection.products_count)
     

  def get_queryset(self,request):
    return super().get_queryset(request).annotate(
      products_count=Count('product')
    )



