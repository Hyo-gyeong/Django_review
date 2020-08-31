from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length = 100)
    url = models.URLField('Site URL')
    favicon = models.ImageField(upload_to="favi", blank=True, null=True)

    def __str__(self):
        return "이름 : " + self.site_name + ", 주소 : " + self.url #Name Error고치는 법 = self.변수이름 으로 수정
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
        #파이썬에서 *, **는 여러개의 인수, 키워드 인수를 받을 때 사용하는 표시
        #args = arguments 
        #kargs = keyword arguments : (키워드 = 특정 값)형태로 함수 호출 가능 & {'키워드':'특정값'}이렇게 딕셔너리 형태로 함수에 전달됨