from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin.decorators import display
from .models import *
class ShopView(ModelAdmin):
    list_display = ['camp_online_6x','shop_choices', 'quantity', 'color']
admin.site.register(Camp_online_6x)
admin.site.register(Camp_online_64)
admin.site.register(Shop, ShopView)
admin.site.register(Activity_Camp)
# Register your models here.
