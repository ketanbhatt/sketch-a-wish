from __future__ import absolute_import
import random
from django import forms
from .models import Wish, Sketch


class WishForm(forms.ModelForm):
    content = forms.CharField(help_text="Wish away!")

    class Meta:
        model = Wish
        fields = ('content',)


class GetWishForm(forms.ModelForm):
    wish = forms.ModelChoiceField(queryset='', initial=0)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(GetWishForm, self).__init__(*args, **kwargs)
        pk_list = Wish.objects.exclude(wisher=self.request.user).filter(pk__in=Wish.objects.filter(is_live=True, locked=False)[:10].values_list('pk')).values_list('pk', flat=True)
        desired_pk = random.sample(pk_list, 3)
        self.fields["wish"].queryset = Wish.objects.filter(pk__in=desired_pk)

    class Meta:
        model = Sketch
        fields = ('wish',)


class SketchForm(forms.ModelForm):
    wish = forms.ModelChoiceField(queryset='', initial=0)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(SketchForm, self).__init__(*args, **kwargs)
        self.fields["wish"].queryset = Wish.objects.filter(sketcher=self.request.user, sketched=False)

    class Meta:
        model = Sketch
        fields = ('wish', 'sketch_image')
