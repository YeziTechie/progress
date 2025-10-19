from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully!")
    return redirect('login')
