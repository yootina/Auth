from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm
from django.contrib.auth import login as auth_login
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')


    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)




def login(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = CustomUserAuthenticationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'login.html', context)