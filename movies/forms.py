from django import forms
from .models import Movie

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'year', 'runtime', 'language', 'genre', 'posterimage','description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),

            'description': forms.Textarea(attrs={'class': 'form-control'}),

            'posterimage': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),

            'year': forms.NumberInput(attrs={'class': 'form-control'}),

            'runtime': forms.TextInput(attrs={'class': 'form-control'}),

            'language': forms.TextInput(attrs={'class': 'form-control'}),

            'genre': forms.TextInput(attrs={'class': 'form-control'}),
           
        }

class signupform(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput (attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)',  widget=forms.PasswordInput (attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email' : 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
         }



class loginform(forms.Form):
   username = forms.CharField(widget= forms.TextInput(attrs = {'autofocus' : True, 'class':'form-control'}))
   password = forms.CharField (label = _("Password"),strip = False, widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password', 'class':'form-control'}))