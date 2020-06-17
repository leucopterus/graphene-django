import graphene

import ingredients.schema
import questions.schema


class IngredientsQuery(ingredients.schema.Query, graphene.ObjectType):
    pass


class QuestionsQuery(questions.schema.Query, graphene.ObjectType):
    pass


class Query(IngredientsQuery, QuestionsQuery):
    pass


schema = graphene.Schema(query=Query)
