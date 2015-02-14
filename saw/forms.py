from django import forms
from django.contrib.auth.models import User
from saw.models import Wish, Sketch, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('country',)

class WishForm(forms.ModelForm):
    content = forms.CharField(help_text="Wish away!")

    class Meta:
        model = Wish
        fields = ('content',)
