from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from random import randrange
from quiz.models import Question
from quiz.models import Answer
from quiz.forms import AnswersForm
from django import forms


def quiz(request):
    """
    For now, the question is selected randomly.
    To do :
        1) test the value sent by the client, just
        to make sure at least it is a integer
        2) coding a version where the questions are
        displayed in a order.
    """
    if request.method == 'POST':
        try:
            selected_answer = Answer.objects.get(id=request.POST['answer'])
            return redirect('answer', id_answer=selected_answer.id)
        except:
            return redirect('error')
    else:
        questions = Question.objects.all()
        # Select a random question.
        question = questions[randrange(len(questions))]
        answers = question.answer_set.all()
    return render(request, 'quiz/quiz.html', locals())


def answer(request, id_answer):
    answer = Answer.objects.get(id=id_answer)
    question = answer.question
    true_answer = question.answer_set.filter(truth=True)[0]
    return render(request, 'quiz/answer.html', locals())


def contact_quiz(request):
    return render(request, 'quiz/contact_quiz.html')


def error(request):
    return render(request, 'quiz/error.html')
