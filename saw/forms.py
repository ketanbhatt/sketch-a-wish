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

class SketchForm(forms.ModelForm):
    wish = forms.ModelChoiceField(queryset= Wish.objects.filter(pk__in = Wish.objects.filter(locked=False)[:3].values_list('pk')), initial=0)
    title = forms.CharField(help_text='Enter title for your Sketch', required=False)
    image_temp = forms.CharField(help_text='Imagine this is an upload button for image, write anything')

    class Meta:
        model = Sketch
        fields = ('wish', 'title', 'image_temp')
