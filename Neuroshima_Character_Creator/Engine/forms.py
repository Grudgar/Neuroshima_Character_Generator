from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika', max_length=150)
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput(render_value=True))
    first_name = forms.CharField(label='Imię', max_length=150)
    last_name = forms.CharField(label='Nazwisko', max_length=150)
    email = forms.EmailField(label='E-mail')


class LoginForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika', max_length=150)
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput(render_value=True))