from django.contrib import admin
from django.db.models.aggregates import Count
from django.utils.html import format_html,urlencode
from django.urls import reverse
from . import models

# Register your models here.

# custom Filter on Inventory
class InventoryFilter(admin.SimpleListFilter):
  title='inventory'  # title of the filter
  parameter_name='inventory'    # this is used in query string of url

  # this function allows what options should appear under filter
  def lookups(self,request,model_admin):
    # return super().lookups(request,model_admin) # default definition
    # overwrite the lookups
    return [
      ('<10','Low')  # (filter value,human readable form to display)

    ]

  def queryset(self,request,queryset):
    # return super().queryset(request,queryset) # default definition
    # override the logic
    # filtering logic on queryset
    if self.value()=='<10':
      return queryset.filter(inventory__lt=10)
     
# this class helps how we wanna view product on admin page
@admin.register(models.Product) # method-1
class ProductAdmin(admin.ModelAdmin):
  list_display=['title','unit_price','inventory_status','collection_title'] # selecting related obj -collection
  list_editable=['unit_price']
  list_per_page=10
  list_select_related=['collection']
  list_filter=['collection','last_update',InventoryFilter]


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
  list_per_page=10
  ordering=['first_name','last_name']
  # search fields
  search_fields=['first_name__istartswith','last_name__istartswith']
  

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



