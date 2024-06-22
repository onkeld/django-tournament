from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Tournament


class TournamentIndexView(ListView):
    model = Tournament
    paginate_by = 100
    template_name = "tournament/index.html"  # Create your views here.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class TournamentDetailView(DetailView):
    model = Tournament
    # template_name = "tournament/tournament_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
