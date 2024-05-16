from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    # path(
    #     'food/graphql',
    #     GraphQLView.as_view(schema=subs.food.graphql.schema),
    #     name='food-graphql',
    # ),

    # path(
    #     'wine/graphql',
    #     GraphQLView.as_view(schema=subs.wine.graphql.schema),
    #     name='wine-graphql',
    # ),
]
