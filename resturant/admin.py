from django.contrib import admin
from .models import menu_items, Category

# Register your models here.

admin.site.register(menu_items)


admin.site.register(Category)