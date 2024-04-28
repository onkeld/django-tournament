from django.db import models
from django.contrib.auth.models import User


class Tournament(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        start_str = self.start_date.strftime('%Y-%m-%d')
        end_str = self.end_date.strftime('%Y-%m-%d')
        tournament_date = start_str + " - " + end_str
        return tournament_date


class Team(models.Model):
    name = models.CharField("Team Name", max_length=255)  # store team name
    club = models.CharField("Club Name", max_length=255)
    city = models.CharField("City of Origin", max_length=75)
    country = models.CharField(
        "Country of Origin", max_length=255, default="Germany")
    # store the preferred colour scheme of the team (home colours)
    primary_colour = models.CharField("Main Team Colour Scheme", max_length=50)
    # store the alternative colour scheme of the team (away colours)
    secondary_colour = models.CharField(
        "Secondary Team Colour Scheme", max_length=50)
    # Team Leader is an authenticated User, so the leader can edit the team info
    team_manager = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, verbose_name="Team Manager",)
    # TODO: The team needs players. Players may or may not be users of the app as to be able to edit their own info. Many-To-One Relationship to players (A player can only be member of one team, but the team needs many players.).

    def __str__(self):
        return self.name
