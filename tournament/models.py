import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.CharField("House Number", max_length=10)
    postcode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = CountryField(default="DE")

    def __str__(self):
        address = self.street + " " + self.number + ", " + \
            self.postcode + " " + self.city + ", " + self.country.name
        return address


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # A User might have multiple addresses. Also an address could belong to multiple users.
    addresses = models.ManyToManyField(Address)
    # Each user can have one phone number for now - might need changing...
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        profile_string = self.user.first_name + "'s Profile"
        return profile_string


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
    # Team Manager is an authenticated User, so the leader can edit the team info
    team_manager = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, verbose_name="Team Manager",)
    players = models.ManyToManyField(
        User, through="TeamMember", related_name='players')

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.SmallIntegerField("Jersey Number")


class Tournament(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    participants = models.ManyToManyField(Team, through="Participant")

    def clean(self):
        # End_Date has to be later than start_Date
        if self.start_date >= self.end_date:
            raise ValidationError(
                _("Start Date can not be later than End Date."))

    def __str__(self):
        start_str = self.start_date.strftime('%Y-%m-%d')
        end_str = self.end_date.strftime('%Y-%m-%d')
        tournament_date = start_str + " - " + end_str
        return tournament_date


class Participant(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.team.name


class Game(models.Model):
    # A game belongs to a tournament.
    # Each tournament can have many games.
    # Therefore, we define a many-to-one relationship.
    # In case a tournament gets deleted, the games belonging to this
    # tournament can be deleted as well.
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    # Each game is played by two teams. One is considered the home, the other
    # the away team.
    # Both Teams have to be participants of the same tournament. Therefore,
    # Home and Away team are one-to-many relationships to the participants.
    # TODO: Validate that home and away team cannot be the same.
    # We do not want to lose past game info if a team gets deleted from the database. Therefore, we set a "Team Deleted" in case the team does not exist anymore.
    home_team = models.ForeignKey(
        Participant, null=True, related_name="HomeTeam", on_delete=models.SET("Team Deleted"))
    home_goals = models.PositiveSmallIntegerField(default=0)
    away_team = models.ForeignKey(
        Participant, null=True, related_name="AwayTeam", on_delete=models.SET("Team Deleted"))
    away_goals = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.home_team.team.name + " - " + self.away_team.team.name
