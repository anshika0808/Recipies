from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login,authenticate,logout
from django.contrib import messages

# Create your views here.
def home(request):
   
   peoples=[{'name':'aviral','age':32},
            {"name":'anshika','age':8},
            {'name':'meenakshi','age':16},
            {'name':'dinesh','age':20},
            {'name':'sourav','age':23}]
   text="bcsbcjscbjsdchsdchisdijcpidjc[oasxzmmxncjd]hshsajdhaodhajd"
   vegetables=['tomato','carrot','bangel']
   return render(request,'index.html',context={'peoples':peoples,'text':text,'vegetables':vegetables,'page':'home'})

def success(request):
    return HttpResponse("""<h2>Yor are successfull</h2>
                       <br> KIET clg jl jaye
                        <font color="green"> Welcome to freeCodeCamp. </font>
                        
                        <p style="color:red"> TCS gate me chli aye</p>""")

def about(request):
    context={'page': 'about'}
    return render(request,'about.html',context)

def contact(request):
    context={'page': 'contact'}
    return render(request,'contact.html',context)

def registration(request):
    if request.method=='POST':
        first_name =request.POST.get('first name')
        last_name=request.POST.get('last name')
        username=request.POST.get('username')
        Email=request.POST.get('email')
        Password=request.POST.get('password')
        if not username or not Email or not Password:
            return render(request, 'registration.html', {'error': 'All fields are required.'})
        
        if User.objects.filter(username=username).exists():
           messages.error(request, "username already exists.")
           return redirect('/registration/')
           '''return render(request, 'registration.html', {'error': 'Username already exists.'})'''
        if User.objects.filter(email=Email).exists():
           messages.error(request, "Email already exists.")
           return redirect('/registration/')
           '''return render(request, 'registration.html', {'error': 'Email already exists.'})'''
        
        user = User.objects.create_user(username=username, email=Email, first_name= first_name,last_name=last_name)
        user.set_password(Password)
        user.save()
       
        auth_login(request, user)
        return redirect('/')
       
    return render(request, 'registration.html')
    '''if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
           
           
            return redirect('/login/')
        else:
            return HttpResponse("already registered")
    form=UserCreationForm()
    return render(request, 'registration.html')'''


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
           messages.error(request, "Invalid username.")
           return redirect('/login/')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid password.")
            return redirect('/login/')
            ''' return render(request, 'login.html', {'error': 'Invalid username or password.'})'''
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/')