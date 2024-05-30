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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # A User might have multiple addresses. Also an address could belong to multiple users.
    addresses = models.ManyToManyField(Address)
    # Each user can have one phone number for now - might need changing...
    phone_number = PhoneNumberField(blank=True)


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

    def __str__(self):
        start_str = self.start_date.strftime('%Y-%m-%d')
        end_str = self.end_date.strftime('%Y-%m-%d')
        tournament_date = start_str + " - " + end_str
        return tournament_date


class Participant(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
