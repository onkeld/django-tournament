from django.test import TestCase
from ..factories.tournament import TournamentFactory
from faker import Faker
from datetime import date, timedelta
# from tournament.models import Tournament


fake = Faker()


class TournamentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.Tournament = TournamentFactory._meta.model

    def test_crud_tournament(self):
        start_date = date.today()
        end_date = date.today() + timedelta(days=3)
        # create
        tournament = TournamentFactory(
            start_date=start_date, end_date=end_date)
        # read
        self.assertEqual(tournament.start_date, start_date)
        self.assertEqual(tournament.end_date, end_date)
        # update
        tournament.start_date = start_date + timedelta(days=1)
        tournament.save()
        self.assertEqual(tournament.start_date, start_date + timedelta(days=1))

    def test_string_representation(self):
        start_date = date.today()
        end_date = date.today() + timedelta(days=3)
        tournament = TournamentFactory(
            start_date=start_date, end_date=end_date)
        datestring = tournament.start_date.strftime(
            '%Y-%m-%d') + " - " + tournament.end_date.strftime('%Y-%m-%d')
        self.assertEqual(str(tournament), datestring)
