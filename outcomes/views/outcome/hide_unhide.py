from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect

from outcomes.models.outcome import Outcome


class HideOutcome(LoginRequiredMixin, View):
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        outcome = get_object_or_404(Outcome, pk=pk, owner=request.user)
        outcome.is_hided = not outcome.is_hided  # toggle state
        outcome.save()
        return redirect(reverse('outcome_detail', kwargs={'pk': pk}))

    def get(self, request, *args, **kwargs):
        outcome = get_object_or_404(Outcome, pk=self.kwargs['pk'], owner=request.user)
        return render(request, 'hide.html', {'outcome': outcome})
