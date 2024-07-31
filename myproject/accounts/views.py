from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import Signupform,LoginForm


def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method=='POST':
        form =Signupform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    else:
        form=Signupform()
    return render(request,'signup.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')




