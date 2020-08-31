from django import forms
from .models import Blog

class APIpost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'mapPoint']