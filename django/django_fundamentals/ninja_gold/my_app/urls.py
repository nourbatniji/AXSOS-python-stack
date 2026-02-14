from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_money/<str:value>', views.process_money),
    path('reset_game', views.reset_game),
    path('game_conditions', views.game_conditions)
]