from django.db import models

# Create your models here.

class menu_items(models.Model):
       name = models.CharField(max_length=50, blank=False)
       price = models.IntegerField()
       is_avalaible = models.BooleanField(default=True)
       description = models.TextField(max_length=300)
       image = models.ImageField(upload_to='images/menu_items_images', blank=True)
