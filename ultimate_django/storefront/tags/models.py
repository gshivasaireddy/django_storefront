from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# from store import Product
# Create your models here.
class Tag(models.Model):
  label =  models.CharField(max_length=255)

class TaggedItems(models.Model):
  # What tag applied to what object
  tag = models.ForeignKey(Tag,on_delete=models.CASCADE)

  # how to identify the product to which tag is applied
  # M-1 :Concrete Approach. 
  # product =models.ForeignKey(Product)

  # Method-2 : More Generic (can be applied to any Entity)
  # This uses abstraction to make it generic
  # It requires two parameters 
  # 1. Type - (Product, Article,Video,Audio etc.)
  # 2. ID - to retrieve the entity info from the relevant table type
  content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE) # type
  object_id =models.PositiveIntegerField()
  content_object= GenericForeignKey()





