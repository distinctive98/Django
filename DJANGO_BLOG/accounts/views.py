from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else :
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form':form})

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('articles:index')

def quit(request):
    if request.method == 'POST':
        request.user.delete()
    return redirect('articles:index')