from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Tournament


class IndexView(ListView):
    model = Tournament
    paginate_by = 100
    template_name = "tournament/index.html"  # Create your views here.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def detail(request, tournament_id):
    return HttpResponse("You're looking at Tournament %s." % tournament_id)
