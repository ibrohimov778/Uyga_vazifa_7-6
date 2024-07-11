from django.contrib.auth import login
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    print(request.POST)
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return  render(request,  'auth\login.html', context={"massage":"Invalid username or password"})

    return render(request, 'auth\Login.html')


def register_view(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            return render(request,'auth\Register.html',context={"massage_password":"Error password"})
        else:
            if User.objects.filter(username=username).exists():
                return render(request, 'auth\Register.html', context={"massage": "This account is busy"})
            new_user = User(first_name=first_name,last_name=last_name,email=email,username=username)
            new_user.set_password(password)
            new_user.save()
            return redirect('login')


    return render(request, 'auth\Register.html')