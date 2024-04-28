from django.contrib import admin
from .models import Tournament, Team, TeamMember, Participant


class TeamMemberInline(admin.StackedInline):
    model = TeamMember
    extra = 5


class ParticipantInline(admin.StackedInline):
    model = Participant


class TournamentAdmin(admin.ModelAdmin):
    inlines = [ParticipantInline]


class TeamAdmin(admin.ModelAdmin):
    inlines = [TeamMemberInline]


admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Team, TeamAdmin)
