from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d' utilisateur")
    password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']
        help_texts = {'username': None,
                      }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mx-auto w-50 mb-3'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control mx-auto w-50 mb-3'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mx-auto w-50 mb-3'}),
            'email': forms.TextInput(attrs={'class': 'form-control mx-auto w-50 mb-3'})}
