from django.shortcuts import render,redirect
from account.forms import * 
from django.contrib import messages
from account.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from blog.views import *
from django.http import HttpResponse
from blog.models.post import Post
from blog.models.profile import Profile
from blog.forms import *
from django.contrib.auth.decorators import login_required


def home(request):
    context = {
        'posts':Post.objects.all()
        }
    return render(request, 'blog/home.html',context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                messages.error(request, "Password fields don't match")
            else:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                ) 
                user.save() 
                messages.success(request,f'Account created for {user.username}!')
                return redirect('user_account:login')
        else:
            messages.error(request, 'Registration failed. Please enter correct details')

    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'auth/register.html', context)

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email= form.cleaned_data['email'] 
            password = form.cleaned_data['password']
            user = authenticate( email=email, password=password)

            if user:
                if user.is_active: 
                    login(request, user) 
                    return redirect(reverse('user_account:home'))
                else:
                    messages.info(request,'ACCOUNT IS INACTIVE')             
            else: 
                messages.info(request,'Invalid login details supplied!')  
        else:
            form = LoginForm()
        
    context = {'form':form}
    return render(request, 'auth/login.html',context)

@login_required
def logout_view(request):
    logout(request)
    return render(request,"auth/logout.html")


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account is Updated')
            return redirect('user_account:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context={
        'p_form':p_form,
        'u_form':u_form
        }
    return render(request,'blog/profile.html',context)