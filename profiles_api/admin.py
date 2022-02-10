from django.contrib import admin

from profiles_api import models

""" Tells django to use UserProfileModel model to admin web interface"""
admin.site.register(models.UserProfile)
