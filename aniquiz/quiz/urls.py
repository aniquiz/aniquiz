from django.conf.urls import url
from django.urls import path

from quiz import views

urlpatterns = [
    url(r'^$', views.first_question, name="first_question"),
    path('question/<int:question_number>/?', views.quiz, name="quiz"),
    url(r'^contact/?$', views.contact_quiz, name="contact_quiz"),
    url(r'^error/?$', views.error, name="error"),
    path('answer/<int:id_answer>/?', views.answer, name="answer"),
]
