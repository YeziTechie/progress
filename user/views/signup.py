from django.shortcuts import render, redirect
from user.forms.signup import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'sign-up.html', {'form': form})
