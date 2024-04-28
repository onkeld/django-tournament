from django.contrib import admin
from .models import Tournament, Team, TeamMember


class TeamMemberInline(admin.StackedInline):
    model = TeamMember
    extra = 5


class TeamAdmin(admin.ModelAdmin):
    inlines = [TeamMemberInline]


admin.site.register(Tournament)
admin.site.register(Team, TeamAdmin)
