from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название опроса', null=False)
    start_date = models.DateTimeField(auto_now_add=True, verbose_name='Время начала', null=False)
    end_date = models.DateTimeField(verbose_name='Время окончания', null=False)
    description = models.TextField(verbose_name='Описание', null=False)

    def __str__(self):
        return f'{self.title}'


class Question(models.Model):
    TYPE_CHOICES = [
        ('TEXT', 'Text answer'),
        ('ONE', 'One answer'),
        ('MULTIPLE', 'Multiple answers'),
    ]

    text = models.CharField(max_length=512, null=False, verbose_name='Текст вопроса')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, related_name='questions_from_quiz', blank=True)
    answer_type = models.CharField(max_length=64, choices=TYPE_CHOICES, verbose_name='Тип ответа')

    def __str__(self):
        return f'{self.text}'


class Answer(models.Model):
    text = models.CharField(max_length=512, null=True, verbose_name='Текст ответа')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name='question_answers')
    responded_users = models.ManyToManyField(User, through='UserAnswersRelation', related_name='answers')

    def __str__(self):
        return f'{self.text}'


class UserAnswersRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.answer}'
