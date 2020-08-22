from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    ordering = ('user',)


admin.site.register(Profile, ProfileAdmin)
