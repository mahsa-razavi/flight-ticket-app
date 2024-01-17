from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import auth
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except ValidationError as e:
                form.add_error('username', e.message)
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')