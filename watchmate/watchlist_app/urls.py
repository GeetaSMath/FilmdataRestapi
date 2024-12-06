from django.urls import path, include

from watchlist_app.views import movie_list,movie_detailes

urlpatterns = [

    path('list/', movie_list, name='movie_list'),
    path('<int:pk>',movie_detailes,name='movie_detailes')

]






