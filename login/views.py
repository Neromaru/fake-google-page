from django.views.generic import CreateView

from login.forms import CredentialForm
from login.models import CredentialModel


class CreateCredentialView(CreateView):
    form_class = CredentialForm
    model = CredentialModel
    template_name = 'index.html'
