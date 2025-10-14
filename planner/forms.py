from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Trip, Review

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['title', 'destination', 'start_date', 'end_date', 'budget', 'description', 'is_public']
        widgets ={
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'review': forms.Textarea(attrs={'row': 4, 'placeholder': 'Write a review or notes about the trip'}),
            'budget': forms.NumberInput(attrs={'placeholder': 'Enter budget in JD '})
        
        }

# sign up form with only username email password 
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required= True)

    class Meta:
        models = User
        fields = ['username', 'email', 'password1','password2']


#login form with user name and password
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Write your review...',
                'class': 'form-control'
            }),
            'rating': forms.NumberInput(attrs={
                'min': 1, 'max': 5, 'class': 'form-control'
            }),
        }