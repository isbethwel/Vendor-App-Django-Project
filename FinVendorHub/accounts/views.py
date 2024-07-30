from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                auth_login(request, user)
                return redirect('login')  # Redirect users to the login page
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('vendor_list')  # Redirect to the vendor list page
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')
