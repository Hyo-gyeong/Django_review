from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    #First of all timezone.now() is just an "improved" version of datetime.datetime.now() that's also timezone aware.
    # timezone.now()
    # >>> datetime.datetime(2015, 9, 10, 19, 45, 34, 105121, tzinfo=<UTC>)
    # datetime.datetime.now()
    # >>> datetime.datetime(2015, 9, 10, 19, 45, 48, 356860)

    was_published_recently.admin_order_field = 'pub_date'#정렬기준항목 설정
    was_published_recently.boolean = True#True면 아이콘 나타남
    was_published_recently.short_description = 'Published recently?'#항목 이름 설정

class Choice(models.Model):
    option = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text