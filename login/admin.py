from django.contrib import admin

from login import models


@admin.register(models.CredentialModel)
class CredentialAdmin(admin.ModelAdmin):
    pass
