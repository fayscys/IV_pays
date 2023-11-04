from django.urls import path
from .views import UserRegistrationView, UserSignInView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('signin/', UserSignInView.as_view(), name='user-signin'),
]