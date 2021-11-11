from django.contrib import admin

from core.models import Quiz, Question, Answer, UserAnswersRelation


class QuestionInline(admin.TabularInline):
    model = Question


class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(UserAnswersRelation)
class UserAnswersRelationAdmin(admin.ModelAdmin):
    pass
