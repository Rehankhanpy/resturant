from django.urls import path
from . import views

urlpatterns = [
       path('', views.index, name='index'),
       path('about', views.about, name='about'),
       path('book', views.book, name='book'),
       path('menu', views.menu, name='menu'),
       path('signup', views.signup, name='signup'),
       path('signin', views.signin, name='signin'),
       path('logout', views.logout_user, name='logout_user'),

]
