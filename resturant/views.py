from django.shortcuts import render, redirect
from .models import menu_items, Category, account, Table, book_table
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



def _create_table(request):
       Table = request.session.session_key
       if not Table:
              Table = request.session.create()
       return Table



def book(request):
       if request.method == 'POST':
              date      = request.POST['datetime']
              no_of_ppl = request.POST['no_of_people']
              

              table = book_table.objects.create(
                     reserved_for = request.user,
                     sheduled_for = date,
                     people       = no_of_ppl,

              )
              table.save()
              
              messages.success(request, 'Table Booked Successfully :)')
              return redirect('/')
              

       return render(request, 'book.html', {'site_details':site_details})

def signup(request):
       if request.user.is_authenticated:
              messages.info(request, 'User is Already Logged In')
              return redirect('/')
       else:
              if request.method == 'POST':  
                     form = SignUpForm(request.POST)  
                     if form.is_valid():  

                            username = request.POST["username"]
                            email = request.POST["email"]
                            phone_number = request.POST["phone_number"]
                            password1 = request.POST["password1"]
                            password2 = request.POST["password2"]

                            if password1 == password2:
                                   #form.save()  

                                   user = account.objects.create_user(username=username, password=password1, email=email)
                                   user.phone_number = phone_number
                                   user.is_active = True
                                   user.save()
                                   messages.success(request, 'Account created successfully')  

                            else:
                                   messages.error(request, 'Passwords Are Not Same')
                            
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
                     email = request.POST["email"]
                     print(username, email, password)

                     User = authenticate(request, email=email, password=password)
                     if User is not None:
                            login(request, User)
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