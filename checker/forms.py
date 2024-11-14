# # forms.py
# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# # from .models import User
# from .models import CustomUser
# from django.contrib.auth import get_user_model

# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password1', 'password2')
#      # Make username and email required
#         labels = {'username': 'Username', 'email': 'Email'}
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#         }

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(max_length=255, required = 'True')
#     password = forms.CharField(max_length=255, required = 'True', widget=forms.PasswordInput)

from django import forms
from .models import CustomUser

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)