from django.contrib import admin

from .models import User, Question, Answer, questionAnswer, Quiz

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(questionAnswer)
admin.site.register(Quiz)
