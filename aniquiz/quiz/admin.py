from django.contrib import admin

from quiz.models import  Question
from quiz.models import  Answer
from quiz.models import  Animation

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'date', 'number')
    list_filter = ('text','date', 'number')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'date', 'animation',
                    'question', 'number',
                    'truth', 'explanation')
    list_filter = ('text','date', 'number', 'truth', 'question')

class AnimationAdmin(admin.ModelAdmin):
    list_display = ('image', 'id',)
    list_filter = ('image', 'id',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Animation, AnimationAdmin)
