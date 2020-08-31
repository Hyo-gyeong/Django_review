from django  import forms
from .models import Portfolio

class NewPofol(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title','body','image']