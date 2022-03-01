from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.


admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ContactMessage)
admin.site.register(Basket)
