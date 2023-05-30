from rest_framework import serializers

from .models import User, Quiz, Question


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('userName', 'email', 'name', 'surName', 'isActive', 'registrationDate')

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ('question', 'author')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('tekst', 'author', 'shuffleAnswers')