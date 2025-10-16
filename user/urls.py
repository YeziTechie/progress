from django.urls import path

from user.views.profile import UserProfileView
from user.views.signup import signup_view
from user.views.login import login_view
from user.views.logout import logout_view


urlpatterns = [
    path('', UserProfileView.as_view(), name='profile'),
    path('sign-up/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
