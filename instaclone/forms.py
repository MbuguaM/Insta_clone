from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Image, Comments, User_prof
from django.forms.widgets import PasswordInput, TextInput


class SignUpForm(UserCreationForm):
    """ form for generating the user """
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(
        attrs={'class': 'validate', 'placeholder': ' Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': ' Password'}))

# updating user 
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('first_name','last_name','email')

# updating the profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model= User_prof
        fields = ['username','bio','prof_photo']

# for the iMage class
class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields = ['image_name','image_caption','image']

# for the comments class
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields = ['comment']