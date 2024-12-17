from django.urls import path, include

from watchlist_app.api.views import movie_list, movie_deatils

urlpatterns = [

    path('list/', movie_list, name='movie_list'),
    path('<int:pk>', movie_deatils, name='movie_detailes')

]