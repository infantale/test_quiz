from django.urls import path

from core.views import ListActiveQuizView, DoneQuizView

from core.views import vote_view

urlpatterns = [
    path('active_quizzes/', ListActiveQuizView.as_view()),
    path('done_quiz/<int:user_id>/', DoneQuizView.as_view(), name='vote_view'),
    path('questions/<int:question_id>/vote/', vote_view, name='vote_view'),
]