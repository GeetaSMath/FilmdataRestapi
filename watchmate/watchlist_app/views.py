from django.shortcuts import render

from watchlist_app.models import Movie
from django.http import JsonResponse


# Create your views here.
def movie_list(requests):
    movies = Movie.objects.all()
    print(movies)
    data = {'movies': list(movies.values())}
    print(data)

    return JsonResponse(data)

