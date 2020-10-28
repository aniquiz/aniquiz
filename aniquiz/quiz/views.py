from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from random import randrange
from quiz.models import Question
from quiz.models import Answer
from quiz.forms import AnswersForm
from django import forms


#def quiz(request):
def quiz(request, question_number):
    """
    """
    if request.method == 'POST':
        try:
            questions = Question.objects.all()
            question = questions[question_number]
            answers = question.answer_set.all()
            selected_answer = answers.get(number=request.POST['answer'])
            return redirect('answer', id_answer=selected_answer.id)
        except:
            return redirect('error')
    else:
        questions = Question.objects.all()
        try:
            question = questions[question_number]
        except:
            question = questions[0]

        answers = question.answer_set.all()
    return render(request, 'quiz/quiz.html', locals())


def answer(request, id_answer):
    answer = Answer.objects.get(id=id_answer)
    """
    Pour une raison que j'ignore,
    je n'arrive pas a avoir la question
    lié à la réponse.
    """
    question = answer.question
    true_answer = question.answer_set.filter(truth=True)[0]
    next_question_number = question.number + 1
    return render(request, 'quiz/answer.html', locals())


def contact_quiz(request):
    return render(request, 'quiz/contact_quiz.html')


def error(request):
    return render(request, 'quiz/error.html')

def first_question(request):
    return redirect('quiz', question_number=0)
