from django.urls import path

from user.views.profile import UserProfileView
from user.views.signup import signup


urlpatterns = [
    path('', UserProfileView.as_view(), name='profile'),
    path('sign-up/', signup, name='signup'),
]
