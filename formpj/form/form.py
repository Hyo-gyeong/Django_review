#model에 있는 내용을 사용하려고 model과 같은 위치에 만들어 줌.
#다른 class에 있는것을 사용하고 싶으면 거기에 만들어주면 됨.(위치가 중요하지는 않음)

from django import forms #장고의 기본기능이니까 django에서 import
from .models import Blog

class BlogPost(forms.ModelForm): #model을 기반으로 하고싶을 때, 그냥 새롭게 임의로 만들고 싶으면 froms.Form
    # email = forms.EmailField()
    # files = forms.FileField()
    # url = forms.URLField()
    # words = forms.CharField(max_length=200)
    # max_number = forms.ChoiceField(choices=[('1', 'one'), ('2', 'two')]) #one을 1로 간주 
    class Meta:
        model = Blog
        fields = ['title', 'photo', 'body']