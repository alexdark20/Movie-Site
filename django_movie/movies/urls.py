from django.urls import path
from django.contrib import admin
from.views import *





urlpatterns = [
    path('',Main.as_view(),name='main'),
    path('film/<int:id>/',FilmDetail.as_view(),name='film_detail_url'),
    path('genre/<str:url>/',GenreDetail.as_view(),name='genre_detail_url'),
    path('actor/<int:id>/',ActorDetail.as_view(),name='actor_detail_url'),
    path('raiting/',AddRating.as_view(),name='film_raiting'),
    path('login/',LoginUser.as_view(),name='login'),
    path('logout/',logout_user,name='logout'),
    path('register/',RegisterUser.as_view(),name='register'),
]
admin.site.site_title = 'Movies'
admin.site.site_header= 'Movies'