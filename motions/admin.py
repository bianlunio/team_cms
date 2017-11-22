from django.contrib import admin

from .models import Motion, TeamMotion


@admin.register(Motion)
class MotionAdmin(admin.ModelAdmin):
    pass


@admin.register(TeamMotion)
class TeamMotionAdmin(admin.ModelAdmin):
    pass
