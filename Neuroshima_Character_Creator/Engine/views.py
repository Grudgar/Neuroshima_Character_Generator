from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Characters
from .forms import RegisterForm, LoginForm

# Create your views here.

class Welcome(View):
    def get(self, request):
        """ Checking if user was logged in already from cookies. """
        user = request.COOKIES.get('logged_in')
        if user is None:
            msg = 'Witaj Gościu! Kliknij przycisk "Zarejestruj" bądź "Zaloguj", aby rozpocząć przygodę z naszym kreatorem!'
        else:
            msg = f'Witaj {user}! Kliknij "Przejdź dalej", aby wrócić do swojej przygody'
        return render(request, 'welcome.html', context={'msg': msg, 'user': user})


class Login(View):
    def get(self, request):
        welcome = 'Proszę wprowadź login i hasło, aby uzyskać dostęp do kreatora.'
        form = LoginForm()
        return render(request, 'login.html', context={'welcome': welcome, 'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                response = HttpResponse('Zalogowano!')
                login(request, user)
                exp = datetime.now() + timedelta(days=1)
                response.set_cookie('logged_in', username, expires=exp)
                return redirect('welcome')
            else:
                response = HttpResponse('Błąd logowania! Albo zapomniałeś hasła, albo nie wiesz jak się nazywasz Podróżniku!')
                response.delete_cookie('logged_in')
                return response



class Register(View):
    def get(self,request):
        form = RegisterForm
        msg = 'Wprowadź poniższe dane aby zarejestrować nowe konto użytkownika'
        return render(request, 'register.html', context={'msg': msg, 'form': form})

    def post(self,request):
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
        try:
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            user.save()
        except Exception:
            return HttpResponse('Użytkownik już istnieje!')




class UserPanel(View):
    def get(self,request):
        """ Listing all the Users characters. """
        user = request.COOKIES.get('logged_in')
        user_id = User.objects.filter(username=user)
        characters = Characters.objects.filter(user_id=user_id)
        return render(request, 'user_panel.html', context={'characters': characters, 'user': user})


class CharCard(View):
    def get(self,request):
        """ Single Character info."""
        char_id = request.GET.get('id')
        char = Characters.objects.filter(char_id=char_id)
        return render(request, 'char_card.html', context={'char': char})