from django.shortcuts import render
from .models import menu_items, Category


site_details = {
       'name':'Restaurant',
       # 'year':date.today.year(),
       'phone':'+92 333333333',
       'email':'xyz@gmail.com'
}

def index(request):
       return render(request, 'index.html', {'site_details':site_details})
       
def about(request):
       return render(request, 'about.html', {'site_details':site_details})

def menu(request):
       items = menu_items.objects.all()
       categories = Category.objects.all()
       return render(request, 'menu.html', {
              'site_details':site_details,
              'items':items,
              'categories':categories,
       })

def book(request):
       return render(request, 'book.html', {'site_details':site_details})
