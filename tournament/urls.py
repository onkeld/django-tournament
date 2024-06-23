from django.urls import path
from .views import TournamentIndexView
from . import views
urlpatterns = [
    path("", TournamentIndexView.as_view(), name="index"),
    path("<int:tournament_id>/", views.TournamentDetail, name="tournament_detail"),
    # path("<pk>/", TournamentDetailView, name="detail"),
]
