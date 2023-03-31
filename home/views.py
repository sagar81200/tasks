from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.core.mail import send_mail


def index(request):
    return render(request, ("index.html"))


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if password != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')
    return render(request, 'register.html')


def login_me(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        obj = authenticate( username=username, password=pass1)
        
        if obj is not None:
            login(request, obj)
            return redirect('blog')
        else:
            return HttpResponse("Username or Password is  not correct!!!")

    return render(request, 'login.html')


def blog(request):
    return render(request, ("blog.html"))

def myblog(request):
    return render(request, ("myblog.html"))


def about(request):
    return render(request, ("about.html"))


def contact(request):
    send_mail(
        'I have a Querry',
        'Hii i have no Querry',
        '8120080600sagar',
        ['7566336576sagar@gmail.com'],
        fail_silently=False,
    )
    return render(request, ("contact.html"))

def features(request):
    return render(request, ("features.html"))

def profile(request):
    return render(request, ("profile.html"))

def details(request):
    if request.method == 'POST':
        age = request.POST.get('Age')
        gender = request.POST.get('Gender')
        mob = request.POST.get('Mob.No.')

        user = Details.objects.create(age=age,gender=gender,mobile=mob)
        user.save()
    return render(request, ('profile.html'))

def write(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        name = request.POST.get('name')
        user = Blog_Post.objects.create_user(text=text,title=name)
        user.save()
    return render(request, ('blog.html'))



def get_blog_post(request):

   
   queryset = Blog_Post.objects.filter(is_approved=True)

   return render(request, 'your_html.html', {'queryset' : queryset})