from django import forms
from django.forms import RadioSelect
from django.forms import ModelForm

from quiz import models
from quiz.models import Answer
from quiz.models import Question

class AnswersForm(forms.Form):
    """
    This is the only way I found to
    generate the choice field with the
    differents answers. I thought that
    maybe those request to the db
    could be done in the view file but,
    can't managed to change the text attribute
    from the view after instancing the form.
    """
#    answers = Answer.objects.all()
#    choices = []
#    for answer in answers:
#        choices.append((answer.number, answer.text))
#    text = forms.ChoiceField(choices=choices,
#                             widget=forms.RadioSelect)

    TEXT_1 = "A"
    TEXT_2 = "B"
    TEXT_3 = "C"
    TEXT_4 = "D"

    CHOICES = [
        ('1', TEXT_1),
        ('2', TEXT_2),
        ('3', TEXT_3),
        ('4', TEXT_4),
    ]
    text = forms.ChoiceField(choices=CHOICES,
                             widget=forms.RadioSelect)
