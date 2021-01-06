from django.forms import ModelForm

from login.models import CredentialModel


class CredentialForm(ModelForm):
    class Meta:
        model = CredentialModel
        fields = ('username', 'password')
    