"""
WSGI config for subs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

import ariadne.wsgi
import subs.food.graphql
import subs.wine.graphql
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'subs.settings')


food_graphql = ariadne.wsgi.GraphQL(
    subs.food.graphql.schema,
    debug=True,
)
wine_graphql = ariadne.wsgi.GraphQL(
    subs.wine.graphql.schema,
    debug=True,
)

django_application = get_wsgi_application()


def application(environ, start_response):
    path_info = environ.get('PATH_INFO', '')

    if path_info.startswith('/food/graphql'):
        return food_graphql(environ, start_response)
    elif path_info.startswith('/wine/graphql'):
        return wine_graphql(environ, start_response)
    else:
        return django_application(environ, start_response)
