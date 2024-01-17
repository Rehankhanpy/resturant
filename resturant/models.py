from django.db import models

# Create your models here.

class Category(models.Model):
       name = models.CharField(max_length=100)

       def __str__(self) :
              return self.name

class menu_items(models.Model):
       name = models.CharField(max_length=50, blank=False)
       price = models.IntegerField()
       menu_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
       is_avalaible = models.BooleanField(default=True)
       description = models.TextField(max_length=300)
       image = models.ImageField(upload_to='images/menu_items_images', blank=True)

       def __str__(self):
              return self.name
