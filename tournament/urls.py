from django.urls import path
from .views import TournamentIndexView, TournamentDetailView
from . import views
urlpatterns = [
    path("", TournamentIndexView.as_view(), name="index"),
    path("<pk>/", TournamentDetailView.as_view(), name="detail"),
]
