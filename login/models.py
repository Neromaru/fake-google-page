from django.db import models


# Create your models here.
class CredentialModel(models.Model):
    username = models.EmailField()
    password = models.TextField()
