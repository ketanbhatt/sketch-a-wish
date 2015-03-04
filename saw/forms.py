from django import forms
from saw.models import Wish, Sketch


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
        self.fields["wish"].queryset = Wish.objects.exclude(wisher=self.request.user).filter(pk__in=Wish.objects.filter(locked=False)[:3].values_list('pk'))

    class Meta:
        model = Sketch
        fields = ('wish',)


class SketchForm(forms.ModelForm):
    wish = forms.ModelChoiceField(queryset='', initial=0)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(SketchForm, self).__init__(*args, **kwargs)
        self.fields["wish"].queryset = Wish.objects.filter(sketcher=self.request.user).filter(sketched=False)

    class Meta:
        model = Sketch
        fields = ('wish', 'sketch_image')
