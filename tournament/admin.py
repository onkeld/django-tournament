from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .models import Tournament, Team, TeamMember, Participant, Address, Profile


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]


class TeamMemberInline(admin.StackedInline):
    model = TeamMember
    extra = 5


class ParticipantInline(admin.StackedInline):
    model = Participant


class TournamentAdmin(admin.ModelAdmin):
    inlines = [ParticipantInline]


class TeamAdmin(admin.ModelAdmin):
    inlines = [TeamMemberInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Profile)
