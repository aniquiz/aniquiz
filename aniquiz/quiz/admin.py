from django.contrib import admin

from quiz.models import  Question
from quiz.models import  Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'date')
    list_filter = ('text','date')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'date', 'image',
                    'question', 'number',
                    'truth', 'explanation')
    list_filter = ('text','date', 'number', 'truth')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
