from django import forms
from .models import Themes, Comments


class CreateThemeForm(forms.ModelForm):
    title = forms.CharField(label='タイトル')

    class Meta:
        model = Themes
        fields = ('title',)