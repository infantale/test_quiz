from datetime import datetime

from django.db.models import F
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Quiz, Question, Answer, UserAnswersRelation

from core.serializers import QuizSerializer, QuestionSerializer, VoteSerializer, UserAnswersRelationSerializer

from core.permissions import IsAdminOrReadOnly


class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAdminOrReadOnly,]


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminOrReadOnly,]


class ListActiveQuizView(ListAPIView):
    queryset = Quiz.objects.filter(end_date__gt=datetime.now())
    serializer_class = QuizSerializer


class DoneQuizView(GenericAPIView):
    serializer_class = UserAnswersRelationSerializer

    def get(self, request, user_id):
        queryset = UserAnswersRelation.objects.filter(user_id=user_id).select_related('answer').annotate(quizzz=F('answer__question__quiz__title'))
        serializer_data = UserAnswersRelationSerializer(queryset, many=True)
        return Response(serializer_data.data)


@api_view(['PATCH'])
# Голосуем по айдишнику вопроса
def vote_view(request, question_id):
    question = UserAnswersRelation.objects.get_or_create(user_id=1, answer_id=request.data['choice_id'])
    serializer = VoteSerializer(data=request.data)
    if serializer.is_valid():
        return Response("Voted")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)