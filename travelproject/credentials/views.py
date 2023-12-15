from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authentication(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
        return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        Password1 = request.POST['Password1']
        Password2 = request.POST['Password2']
        if Password1 == Password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User name already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=Password1, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save();
                return redirect('login')
            print("User Created")
        else:
            messages.info(request, "Password deos not match ")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")

def logout(request):
    auth.login(request)
    return render('/')
