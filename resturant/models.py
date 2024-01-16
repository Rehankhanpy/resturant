from django.db import models

# Create your models here.

class menu_items(models.Model):
       name = models.CharField(max_length=50, blank=False)
       price = models.IntegerField()
       choices = {
              'Burger':'Burger',
              'Pizza':'Pizza',
              'Pasta':'Pasta',
              'Fries':'Fries'
       }
       category = models.CharField(max_length=10, blank=True, null=True, choices=choices)
       is_avalaible = models.BooleanField(default=True)
       description = models.TextField(max_length=300)
       image = models.ImageField(upload_to='images/menu_items_images', blank=True)

       def __str__(self):
              return self.name
