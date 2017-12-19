from django.contrib import admin

from core.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """
    Profile Admin View

    """
    list_display = ('uuid', 'user', 'location', 'birth_date')


admin.site.register(Profile, ProfileAdmin)
