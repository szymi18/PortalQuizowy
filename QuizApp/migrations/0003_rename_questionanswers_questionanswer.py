# Generated by Django 4.2.1 on 2023-05-16 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0002_questionanswers_iscorrect_alter_answer_author_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='questionAnswers',
            new_name='questionAnswer',
        ),
    ]
