from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.api.serializers import MovieSearializer
from watchlist_app.models import Movie


@api_view()
def movie_list(requests):
    movies = Movie.objects.all()
    serializers = MovieSearializer(movies, many=True)
    return Response(serializers.data)


@api_view()
def movie_deatils(request, pk):
    movies = Movie.objects.get(pk=pk)
    serializers = MovieSearializer(movies)
    return Response(serializers.data)
