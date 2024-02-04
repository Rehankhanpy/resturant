from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import menu_items, Category, account, Table, book_table

# Register your models here.
class accountadmin(UserAdmin):
       list_display = ['username', 'email']
       list_display_links = ['username', 'email']
       readonly_fields = ['last_login', 'date_joined']
       ordering = ('-username',)

       filter_horizontal = ()
       list_filter = ()
       fieldsets = ()

class menu_items_admin(admin.ModelAdmin):
       list_display = ['name', 'price', 'is_avalaible']


class table_admin(admin.ModelAdmin):
       list_display = ['no_of_tables']


class book_table_admin(admin.ModelAdmin):
       list_display = ['reserved_for', 'people', 'sheduled_for']
       

admin.site.register(menu_items, menu_items_admin)
admin.site.register(account, accountadmin)
admin.site.register(Category)
admin.site.register(book_table, book_table_admin)
admin.site.register(Table, table_admin)