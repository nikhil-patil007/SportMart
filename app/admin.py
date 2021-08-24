from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(seller)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Rating)
admin.site.register(Cart)