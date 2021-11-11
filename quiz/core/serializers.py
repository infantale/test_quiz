from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from core.models import Quiz, Question, Answer, UserAnswersRelation


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ('text', 'question', 'responded_users')


class QuestionSerializer(ModelSerializer):
    question_answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('text', 'quiz', 'answer_type', 'question_answers')

    def create(self, validated_data):
        answers_data = validated_data.pop('question_answers')
        question = Question.objects.create(**validated_data)
        for answer_data in answers_data:
            Answer.objects.create(question=question, **answer_data)
        return question

    def update(self, instance, validated_data):
        answers_data = validated_data.pop('question_answers')
        print(dir(instance))
        print(instance.question_answers)
        answers = instance.question_answers.all()
        print(answers, instance)
        answers = list(answers)
        instance.text = validated_data.get('text', instance.text)
        instance.quiz = validated_data.get('quiz', instance.quiz)
        instance.answer_type = validated_data.get('answer_type', instance.answer_type)
        instance.save()

        for answer_data in answers_data:
            answer = answers.pop()
            answer.text = answer_data.get('text', answer.text)
            answer.question = answer_data.get('question', answer.question)
            answer.save()

        return instance


class QuizSerializer(ModelSerializer):
    start_date = serializers.DateTimeField(read_only=True)
    questions_from_quiz = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['title', 'start_date', 'end_date', 'description', 'questions_from_quiz']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions_from_quiz')
        quiz = Quiz.objects.create(**validated_data)
        for question_data in questions_data:
            Question.objects.create(quiz=quiz, **question_data)
        return quiz

    def update(self, instance, validated_data):
        questions_data = validated_data.pop('questions_from_quiz')
        questions = instance.questions_from_quiz.all()
        questions = list(questions)
        instance.title = validated_data.get('title', instance.title)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        for question_data in questions_data:
            question = questions.pop()
            question.text = question_data.get('text', question.text)
            question.quiz = question_data.get('quiz', question.quiz)
            question.answer_type = question_data.get('answer_type', question.answer_type)
            question.save()

        return instance


class VoteSerializer(Serializer):
    choice_id = serializers.IntegerField()


class UserAnswersRelationSerializer(ModelSerializer):
    quizzz = serializers.CharField(read_only=True)

    class Meta:
        model = UserAnswersRelation
        fields = ('user', 'answer', 'quizzz')
