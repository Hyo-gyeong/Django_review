from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    #StackedInlne은 세로로 보임
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question']}),
        ('Date information', {'fields':['pub_date']}),
    ]

    list_display = ('question', 'pub_date', 'was_published_recently')

    inlines = [ChoiceInline]

    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Question, QuestionAdmin) #위에서부터 읽어내려오기때문에 QuestionAdmin정의 밑에 적어줘야함