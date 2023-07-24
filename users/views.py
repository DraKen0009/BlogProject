from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import UserRegisterForm ,ProfileUpdateForm,UserUpdateForm
from django.contrib import messages
from .models import Profile
# Create your views here.

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Succesfully registered")
            return redirect('login')

    else:
        form=UserRegisterForm()

    context={
        'form':form
    }
    return render(request,'users/register.html',context)


@login_required
def profile(request):
    return render(request,'users/profile.html')\

@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request,"Successfully updated your profile")
            return redirect('profile')
    else:
        u_form = UserUpdateForm( instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context={
        'p_form':p_form,
        'u_form':u_form
    }
    return render(request, 'users/update_profile.html', context)