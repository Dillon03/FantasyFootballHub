from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-player/', views.add_player, name='add_player'),
    path('team/<int:team_id>/', views.manage_roster, name='manage_roster'),
    path('player/<int:player_id>/edit/', views.edit_player, name='edit_player'),
    path('player/<int:player_id>/remove/', views.remove_player, name='remove_player'),
    path("create-team/", views.create_team, name="create_team"),
]