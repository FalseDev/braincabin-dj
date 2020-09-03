from graphene import ObjectType, Schema, String


def resolve_hello(root, info, name):
    return f"Nishe {name}"


def resolve_goodbye(root, info):
    return 'Goodbye'


class Query(ObjectType):
    hello = String(name=String(default_value="Unknown"))
    goodbye = String()

    resolve_hello = resolve_hello
    resolve_goodbye = resolve_goodbye


schema = Schema(query=Query)