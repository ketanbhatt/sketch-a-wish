from django import forms
from django.db.models import F
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

class GetWishForm(forms.ModelForm):
    wish = forms.ModelChoiceField(queryset= Wish.objects.filter(pk__in = Wish.objects.filter(locked=False)[:3].values_list('pk')), initial=0)

    class Meta:
        model = Sketch
        fields = ('wish',)

class SketchForm(forms.ModelForm):
    wish = forms.ModelChoiceField(queryset= '' , initial=0)
    image_temp = forms.CharField(help_text='Imagine this is an upload button for image, write anything')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(SketchForm, self).__init__(*args, **kwargs)
        self.fields["wish"].queryset = Wish.objects.filter(sketcher=self.request.user).filter(sketched=False)

    class Meta:
        model = Sketch
        fields = ('wish', 'image_temp')
