from django.urls import path

from pages import views
from spotify.views import home as spotifyhome
from spotify.views import add_data


urlpatterns = [
    path("", views.home, name="home"),
    path("up", views.up, name="up"),
    path("home", spotifyhome, name="spotify"),
    path("data", add_data, name="add_data"),
]
