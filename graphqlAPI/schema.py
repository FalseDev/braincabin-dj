from graphene import ObjectType, Schema, String, List, Field, Int
from graphqlAPI import resolvers
from graphqlAPI import typeDefs


class Query(ObjectType):
    all_questions = Field(List(typeDefs.QuestionType),
                          page=Int(required=False))
    all_profiles = Field(List(typeDefs.ProfileType), page=Int(required=False))

    question = Field(typeDefs.QuestionType, id=Int(required=True))
    user = Field(typeDefs.UserType, id=Int(required=True))

    resolve_all_questions = resolvers.resolve_all_questions
    resolve_all_profiles = resolvers.resolve_all_profiles

    resolve_question = resolvers.resolve_question
    resolve_user = resolvers.resolve_user

class Mutation(ObjectType):
    register = Field(typeDefs.UserType, name=String(required=True), username=String(
        required=True), password=String(required=True), email=String(required=True), date_of_birth=String(required=True))
    login = Field(typeDefs.UserType, username=String(
        required=True), password=String(required=True))

    resolve_register = resolvers.resolve_register
    resolve_login = resolvers.resolve_login


schema = Schema(query=Query, mutation=Mutation)
