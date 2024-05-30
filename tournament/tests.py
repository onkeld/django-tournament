from django.test import TestCase
from datetime import date, timedelta
from .models import Tournament


# Create your tests here.


class TournamentModelTest(TestCase):

    def test_string_representation(self):

        tournament = Tournament(
            start_date=date.today() + timedelta(days=1), end_date=date.today() + timedelta(days=3))
        datestring = tournament.start_date.strftime(
            '%Y-%m-%d') + " - " + tournament.end_date.strftime('%Y-%m-%d')
        self.assertEqual(str(tournament), datestring)
