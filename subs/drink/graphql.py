import pathlib

import ariadne
from ariadne.contrib import federation

BEER_DB = {
    '1': {
        'id': '1',
        'name': 'Chocolate Milk Stout',
        'description': 'Dark.  Not for Stephen.',
        'abv': 7.5,
        'ibu': 40,
    },
    '2': {
        'id': '2',
        'name': 'Modelo Negra',
        'description': 'Tacos rule.',
        'abv': 5.0,
        'ibu': 25,
    },
    '3': {
        'id': '3',
        'name': 'Yuengling',
        'description': 'Apparently pretty good!',
        'abv': 6.0,
        'ibu': 70,
    },
}

WINE_DB = {
    '1': {
        'id': '1',
        'name': 'Pinot Noir',
        'description': 'I am **NOT** drinking a Merlot!',
        'abv': 12.5,
        'notes': 'Musty',
    },
    '2': {
        'id': '2',
        'name': 'Bordeaux',
        'description': 'La France!',
        'abv': 11.0,
        'notes': 'Baguette-y',
    },
    '3': {
        'id': '3',
        'name': 'Ripple',
        'description': 'For emergencies.',
        'abv': 12.0,
        'notes': 'Fortifying',
    },
}


schema_file = pathlib.Path(__file__).parent / 'schema.graphql'
type_defs = ariadne.load_schema_from_path(schema_file)


Query = ariadne.ObjectType("Query")


@Query.field("wines")
def query_wines(root, gqlinfo, **kwargs):
    return list(WINE_DB.values())


@Query.field("beers")
def query_beers(root, gqlinfo, **kwargs):
    return list(BEER_DB.values())


Beer = federation.FederatedObjectType('Beer')
Wine = federation.FederatedObjectType('Wine')


@Beer.reference_resolver
def beer_reference_resolver(root, gqlinfo, representation):
    beer_id = representation.get('id', '')
    beer = BEER_DB.get(beer_id)
    if beer is None:
        print(f'No beer found for {beer_id}.')
    return beer


@Wine.reference_resolver
def wine_reference_resolver(root, gqlinfo, representation):
    wine_id = representation.get('id', '')
    wine = WINE_DB.get(wine_id)
    if wine is None:
        print(f'No wine found for {wine_id}.')
    return wine


schema = federation.make_federated_schema(
    type_defs,
    Beer,
    Wine,
    Query
)
