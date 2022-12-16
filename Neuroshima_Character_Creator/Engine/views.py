from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.views import View
from Neuroshima_Character_Creator.Engine.models import User, Characters

# Create your views here.

class Welcome(View):
    def get(self, request):
        """ Checking if user was logged in already from cookies. """
        user = request.COOKIES.get('logged_in', '0')
        if user == 0:
            msg = 'Witaj Gościu! Kliknij przycisk "Zarejestruj" bądź "Zaloguj", aby rozpocząć przygodę z naszym kreatorem!'
        else:
            msg = f'Witaj {user}! Kliknij "Przejdź dalej", aby wrócić do swojej przygody'
        return render(request, 'welcome.html', context={'msg': msg, 'user': user})


class Login(View):
    def get(self, request):
        welcome = 'Proszę wprowadź login i hasło, aby uzyskać dostęp do kreatora.'
        return render(request, 'login.html', context={'welcome': welcome})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except Exception:
            user = None
        try:
            pass_word = User.objects.get(password=password)
        except Exception:
            pass_word = None
        check = [user, pass_word]
        if all(i is not None for i in check):
            response = HttpResponse('Zalogowano!')
            exp = datetime.now() + timedelta(days=1)
            response.set_cookie('logged_in', username, expires=exp)
            return response
        else:
            response = HttpResponse('Błąd logowania! Albo zapomniałeś hasła, albo nie wiesz jak się nazywasz Podróżniku!')
            response.delete_cookie('logged_in')
            return response


class Register(View):
    pass


class UserPanel(View):
    def get(self,request):
        """ Listing all the Users characters. """
        user = request.COOKIES.get('logged_in')
        user_id = User.objects.get(username=user)
        characters = Characters.objects.filter(user_id=user_id.id)
        return render(request, 'user_panel.html', context={'characters': characters, 'user': user})


class CharCard(View):
    def get(self,request):
        """ Single Character info."""
        char_id = request.GET.get('id')
        char = Characters.objects.filter(char_id=char_id)
        return render(request, 'char_card.html', context={'char': char})