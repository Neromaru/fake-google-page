from django.views.generic import CreateView

from login.forms import CredentialForm
from login.models import CredentialModel
from django.conf import settings


class CreateCredentialView(CreateView):
    form_class = CredentialForm
    model = CredentialModel
    template_name = 'index.html'
    success_url = settings.REDIRECT_URL
