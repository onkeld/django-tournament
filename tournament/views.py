from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.template import loader
from .models import Tournament, Participant


class TournamentIndexView(ListView):
    model = Tournament
    paginate_by = 100
    template_name = "tournament/index.html"  # Create your views here.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def TournamentDetail(request, tournament_id):
    tournament = Tournament.objects.get(pk=tournament_id)
    # participants = tournament.participants.all
    template = loader.get_template("tournament/tournament_detail.html")
    context = {"participants": sorted(
        tournament.participant_set.all(), key=lambda a: (a.calculate_points(), a.calculate_goal_diff()), reverse=True)}

    return HttpResponse(template.render(context, request))


# class TournamentDetailView(DetailView):
#    model = Tournament

 #   def get_context_data(self, **kwargs):
 #       context = super().get_context_data(**kwargs)
 #       return context
