from django.contrib import admin
from . models import Cport
# Register your models here.
@admin.register(Cport)
class CportAdmin(admin.ModelAdmin):
    list_display = ("id", "cmp","email","img",'date')
