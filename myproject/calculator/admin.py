from django.contrib import admin
from .models import Cal
# Register your models here.

@admin.register(Cal)
class CalAdmin(admin.ModelAdmin):
    list_display = ("first_value", 'second_value', 'result')