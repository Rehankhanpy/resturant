from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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


class MyAccountManager(BaseUserManager):
       def create_user(self, username, email, password=None):
              if not email:
                     ValueError('E-mail Address Required')
              if not username:
                     ValueError('Username Required')

              user = self.model(
                     email = self.normalize_email(email),
                     usernaame = username,
                     
              )

              user.set_password(password)
              user.save(using=self._db)
              return user
       
       
       def create_superuser(self, username, email, password):
              user = self.create_user(
                     email = self.normalize_email(email),
                     username = username,
                     password = password,
              )
       
              user.is_admin = True
              user.is_active = True
              user.is_superadmin = True
              user.is_staff = True

              user.save(using=self._db)
              return user
class account(AbstractBaseUser):
       username     = models.CharField(max_length=60)
       email        = models.EmailField(max_length=60, unique=True)
       phone_number = models.CharField(max_length=60)

       #required 
       date_joined   = models.DateTimeField(auto_now_add=True)
       last_login    = models.DateTimeField(auto_now_add=True)
       is_admin      = models.BooleanField(default=False)
       is_superadmin = models.BooleanField(default=False)
       is_staff      = models.BooleanField(default=False)
       is_admin      = models.BooleanField(default=False)

       USERNAME_FIELD  = 'email'
       REQUIRED_FIELDS = ['username', 'email']

       objects = MyAccountManager()

       def __str__(self):
              return self.email
       
       def has_perms(self, perm, obj=None):
              return self.is_admin
       
       def has_module_perms(self, add_label):
              return True
       
