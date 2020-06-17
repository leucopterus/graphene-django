import graphene
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from ingredients.models import Category, Ingredient


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (relay.Node,)


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node,)


class Query(ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)


# first part
# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = Category
#
# class IngredientType(DjangoObjectType):
#     class Meta:
#         model = Ingredient
# class Query(object):
#     category = graphene.Field(CategoryType,
#                               id=graphene.Int(),
#                               name=graphene.String())
#     all_categories = graphene.List(CategoryType)
#     ingredient = graphene.Field(IngredientType,
#                                 id=graphene.Int(),
#                                 name=graphene.String())
#     all_ingredients = graphene.List(IngredientType)
#
#     def resolve_all_categories(self, info, **kwargs):
#         return Category.objects.all()
#
#     def resolve_all_ingredients(self, info, **kwargs):
#         # We can easily optimize query count in the resolve method
#         return Ingredient.objects.select_related('category').all()
#
#     def resolve_category(self, info, **kwargs):
#         id = kwargs.get('id')
#         name = kwargs.get('name')
#
#         if id is not None:
#             return Category.objects.get(pk=id)
#
#         if name is not None:
#             return Category.objects.get(name=name)
#
#         return None
#
#     def resolve_ingredient(self, info, **kwargs):
#         id = kwargs.get('id')
#         name = kwargs.get('name')
#
#         if id is not None:
#             return Ingredient.objects.get(pk=id)
#
#         if name is not None:
#             return Ingredient.objects.get(name=name)
#
#         return None
