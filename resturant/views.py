from django.shortcuts import render, redirect
from .models import menu_items, Category
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


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

def signup(request):
       if request.user.is_authenticated:
              messages.info(request, 'User is Already Logged In')
              return redirect('/')
       else:
              if request.method == 'POST':  
                     form = SignUpForm(request.POST)  
                     if form.is_valid():  
                            form.save()  
                            messages.success(request, 'Account created successfully')  

                            username = request.POST["username"]
                            password1 = request.POST["password1"]

                            user = authenticate(request, username=username, password=password1)
                            if user is not None:
                                   login(request, user)
                                   return redirect('/')
                            
                     else:
                            for errors in form.errors.items():
                                   for error in errors:
                                         messages.error(request, error)
              else:  
                     form = SignUpForm() 
              return render(request, 'signup.html', {'site_details':site_details, 'form':form})

def signin(request):
       if request.user.is_authenticated:
              messages.info(request, 'User is Already Logged In')
              return redirect('/')
       else:
              if request.method == 'POST':
                     username = request.POST["username"]
                     password = request.POST["password"]

                     user = authenticate(request, username=username, password=password)
                     if user is not None:
                            login(request, user)
                            messages.success(request, 'Logged In Successfully')
                            return redirect('/')
                     else:
                            messages.error(request, 'User Not Found')
       return render(request, 'signin.html', {'site_details':site_details,})

def logout_user(request):
       if request.user.is_authenticated:
              logout(request)
              messages.success(request, 'Logged Out Successfully')
              return redirect('/')