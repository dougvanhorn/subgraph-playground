import pathlib

import ariadne
from ariadne.contrib import federation


FOOD_DB = {
    '1': {
        'id': '1',
        'name': 'Spam',
        'description': 'Spiced pork and ham.',
        'bestWith': {
            '__typename': 'Wine',
            'id': '1',
            'extra': 'This is extra data',
        },
    },
    '2': {
        'id': '2',
        'name': 'Eggs',
        'description': 'Pre-chicken units.',
        'bestWith': {
            '__typename': 'Wine',
            'id': '2',
            'extra': 'This is extra data',
        },
    },
    '3': {
        'id': '3',
        'name': 'Bacon',
        'description': 'Swine underbelly.',
        'bestWith': {
            '__typename': 'Beer',
            'id': '3',
            'extra': 'This is extra data',
        },
    },
    '4': {
        'id': '4',
        'name': 'Sea Bass',
        'description': 'Fancy fish.',
        'bestWith': {
            '__typename': 'Beer',
            'id': '1',
            'extra': 'This is extra data',
        },
    },
    '5': {
        'id': '4',
        'name': 'Sea Bass',
        'description': 'Fancy fish.',
        'bestWith': {
            '__typename': 'Beer',
            'id': '2',
            'extra': 'This is extra data',
        },
    },
}


schema_file = pathlib.Path(__file__).parent / 'schema.graphql'
type_defs = ariadne.load_schema_from_path(schema_file)


Query = ariadne.ObjectType("Query")


@Query.field("foods")
def resolve_foods(root, gqlinfo, **kwargs):
    print('ROOT', root)
    print('GQLINFO', gqlinfo)
    print(dir(gqlinfo))
    return list(FOOD_DB.values())


Food = federation.FederatedObjectType("Food")


@Food.reference_resolver
def food_reference_resolver(root, gqlinfo, representation):
    food_id = representation.get('id', '')
    food = FOOD_DB.get(food_id)
    return food


schema = federation.make_federated_schema(
    type_defs,
    Food,
    Query
)
