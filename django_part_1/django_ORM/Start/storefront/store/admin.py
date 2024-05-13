from django.contrib import admin
from . import models

# Register your models here.
# this class helps how we wanna view product on admin page
@admin.register(models.Product) # method-1
class ProductAdmin(admin.ModelAdmin):
  list_display=['title','unit_price','inventory_status']
  list_editable=['unit_price']
  list_per_page=10

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


# let's register our Collection app
admin.site.register(models.Collection)

