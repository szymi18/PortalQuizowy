from django.db import models


class User(models.Model):
    userName = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField
    name = models.CharField(max_length=100)
    surName = models.CharField(max_length=100)
    isActive = models.BooleanField
    registrationDate = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    tekst = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    shuffleAnswers = models.BooleanField(default=True)

class Answer(models.Model):
    tekst = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class questionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    answerOrder = models.IntegerField
    isCorrect = models.BooleanField(default=False)

class Quiz(models.Model):
    class Meta:
        verbose_name_plural = "quizes"
    question = models.ManyToManyField(Question)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)