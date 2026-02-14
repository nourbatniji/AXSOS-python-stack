from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('guess_number', views.guess_number),
    path('play_again', views.play_again),
    path('winners', views.winners),
]