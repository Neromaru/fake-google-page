from django.urls import path

from login.views import CreateCredentialView

urlpatterns = [
    path('sign-in/', CreateCredentialView.as_view(), name='sign_in')
]
