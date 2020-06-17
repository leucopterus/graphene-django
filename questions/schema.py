import graphene
import graphene_django

from graphene_django.types import DjangoObjectType
from .models import Question, QestionCategory


class QuestionType(DjangoObjectType):
    extra_field = graphene.String()

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'category')

    def resolve_extra_field(self, info):
        return 'test'

    @classmethod
    def get_queryset(cls, queryset, info):
        if info.context.user.is_anonymous:
            return queryset.filter(publised=True)
        return queryset


class QuestionCategoryType(DjangoObjectType):

    class Meta:
        model = QestionCategory


class Query:
    questions = graphene_django.DjangoListField(QuestionType)
    question = graphene.Field(QuestionType, question_id=graphene.Int())

    categories = graphene.List(QuestionCategoryType)
    category = graphene.Field(QuestionCategoryType, category_id=graphene.String())

    def resolve_questions(self, info, **kwargs):
        if info.context.user.is_authenticated:
            return Question.objects.all()
        return Question.objects.none()

    def resolve_question(self, info, **kwargs):
        question_id = kwargs.get('question_id')

        if question_id is not None:
            return Question.objects.get(pk=question_id)
        return None

    def resolve_categories(self, info, **kwargs):
        return QestionCategory.objects.all()

    def resolve_category(self, info, **kwargs):
        category_id = kwargs.get('category_id')

        if category_id is not None:
            return QestionCategory.objects.get(pk=category_id)
        return None