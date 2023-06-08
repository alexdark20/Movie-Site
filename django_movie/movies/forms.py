from django import forms
from django.contrib.auth.models import User
from .models import Reviews, Rating, RatingStar
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ReviewsForm(forms.ModelForm):
    class Meta:
        model=Reviews
        fields=['name','email','text']
        widgets={
            'text':forms.Textarea(attrs={'class':'comment-textarea'}),
            'email':forms.EmailInput(attrs={'class':"input-email"}),
            'name':forms.TextInput(attrs={'class':"input-name"}),
        }


class RatingForm(forms.ModelForm):
    star=forms.ModelChoiceField(RatingStar.objects.all(),widget=forms.RadioSelect,empty_label=True)
    class Meta:
        model=Rating
        fields=['star']


class RegisterUserForm(UserCreationForm):
    username=forms.CharField(label='Логін',widget=forms.TextInput(attrs={'class':'form-input'}))
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2=forms.CharField(label='Повторення паролю',widget=forms.PasswordInput(attrs={'class':'form-input'}))
    class Meta:
        model=User
        fields=('username','email','password1','password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

