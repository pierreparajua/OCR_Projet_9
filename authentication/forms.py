from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d' utilisateur")
    password = forms.CharField(widget=forms.PasswordInput, label='mot de passe')