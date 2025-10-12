from django.contrib.auth.forms import UserCreationForm
from user.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','profile_picture','element','animal')
