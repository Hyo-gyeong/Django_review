from django.db import models
#thumbnail
from imagekit.models import ImageSpecField #썸네일 만들기
from imagekit.processors import ResizeToFill #사이즈 조정 쉽게


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    #개발자들이 가장 실수하는 부분은 CharField, TextField와 같은 문자열 기반 필드에 null=True를 정의하는 것이다. 이 같은 실수를 피해야한다. 그렇지 않으면 “데이터 없음”에 대해 두 가지 값, 즉 None 과 빈 문자열 을 갖게된다. “데이터 없음”에 대해 두 가지 값을 갖는 것은 중복이다. 그리고 Null이 아닌 빈 문자열을 사용하는 것이 장고 컨벤션이다.
    #따라서 만약 문자열 기반 모델 필드를 “nullable” 하게 만들고 싶다면 black = True
    photo = models.ImageField(blank=True, upload_to='img')
    # Null : DB와 관련되어 있다. (database-related) 주어진 데이터베이스 컬럼이 null 값을 가질 것인지 아닌지를 정의한다.
    # Blank : 유효성과 관련되어 있다. (validation-related) form.is_valid()가 호출될 때 폼 유효성 검사에 사용된다.
    # 그러므로 즉, null=True, blank=False 옵션을 가진 필드를 정의하는 것에는 문제가 없다. 이는 DB레벨에서는 해당 필드가 NULL 될 수 있지만, application 레벨에서는 required 필드인 것을 의미한다.

    #models.FileField : 파일 저장을 지원하는 모델 필드
    #models.ImageField : 이미지 저장을 지원하는 모델 필드 (FileField 상속)
    thumbnail = ImageSpecField(source='photo', processors=[ResizeToFill(100, 100)], options={'quality':5})
                                    #^^^^^변수 이름             ^^^^^이미지 크기
    #ImageSpecField 다른 기능 1.format으로 확장자 지정 가능 예)format = 'JPEG'
    #                          2.압축방식 예)options={'quality':60}
    pub_date = models.DateTimeField('date published')#DateTimeField에서는 null = True넣을 수 있음
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    #null과 blank 옵션의 티폴트 값은 False 이다.
    #또한 특별한 케이스가 있는데, 만약 BooleanField에 NULL 값을 받고 싶다면, NullBooleanField를 대신 사용하자.