from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import CustomUserCreationForm, CustomUserUpdateForm


@login_required(login_url='login')
def index(request):
    users = User.objects.all()
    return render(request, 'user-home.html', {'users': users})


@login_required(login_url='login')
def user_profile(request):
    user = User.objects.get(id=request.user.id)
    return render(request, 'user-profile.html', {'user': user})


def user_register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error occured during registraion.')

    return render(request, 'user-register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except:
                messages.error(request, "User does not exist.")

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Email or password incorrect.")
        else:
            messages.error(request, "Email or password not provided.")

    return render(request, 'user-login.html', {})


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='user_login')
def user_update(request):
    user = request.user
    form = CustomUserUpdateForm(instance=user)

    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile')

    return render(request, 'user-update.html', {'form': form})
