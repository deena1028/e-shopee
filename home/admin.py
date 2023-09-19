from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import category,product,cart,login1
# Register your models here.
mymodel=[category,product,cart,login1]
admin.site.register(mymodel)