import factory
from faker import Faker
from datetime import timedelta
from tournament.models import Tournament

fake = Faker()


class TournamentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tournament
        django_get_or_create = ('start_date', 'end_date')

    start_date = fake.future_date()
    end_date = start_date + timedelta(days=2)
