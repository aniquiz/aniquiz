from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True,
                                auto_now=False,
                                verbose_name="Date")
    number = models.PositiveSmallIntegerField(blank=False)

class Answer(models.Model):
    text = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True,
                                auto_now=False,
                                verbose_name="Date")
    image = models.ImageField(upload_to="quiz/images/")
    question = models.ForeignKey('Question',
                                 null=True,
                                 on_delete=models.CASCADE,)
    number = models.PositiveSmallIntegerField(blank=False)
    truth = models.BooleanField(blank=False)
    explanation = models.TextField(blank=False, null=True)

    def __def__(self):
        return self.text
    def __str__(self):
        return self.__def__()
