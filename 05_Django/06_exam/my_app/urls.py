from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index),
    path('reg_user', views.register),
    path('login_user', views.login),
    path('logout', views.logout),
    path('dashboard', views.dashboard),
    path('add_game', views.add_game),
    path('game/<int:id>', views.got_to_game),
    path('edit/game/<int:id>', views.go_to_edit),
    path('update_game/<int:id>', views.update_game),
    path('delete_game', views.delete_game),
    path('order_games', views.order_games),
    # path('order_favs', views.order_favs),
    path('add_game_to_favorite', views.add_game_to_favorite),
    path('gamer_details/<int:id>', views.gamer_details),
]