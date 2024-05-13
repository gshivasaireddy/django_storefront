from django.contrib import admin
from . import models


# Register your models here.
# let's register our Collection app
admin.site.register(models.Collection)

# let's register the products app
admin.site.register(models.Product)