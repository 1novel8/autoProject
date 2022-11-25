from django.urls import path, include
from authorization.views import RegistrationUserView


urlpatterns = [
    path('registration/', RegistrationUserView.as_view())
]
