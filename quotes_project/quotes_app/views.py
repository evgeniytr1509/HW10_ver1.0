from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, UserLoginForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('quotes')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def quotes(request):
    # Получаем список всех цитат из базы данных
    all_quotes = Quote.objects.all()

    # Передаем список цитат в шаблон 'quotes.html'
    return render(request, 'quotes.html', {'quotes': all_quotes})