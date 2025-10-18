from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect

from outcomes.models.outcome import Outcome


class SetAsAchieved(LoginRequiredMixin, View):
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        outcome = get_object_or_404(Outcome, pk=pk, owner=request.user)
        outcome.is_achieved = not outcome.is_achieved  # toggle achieved
        outcome.achieved_at = timezone.now() if outcome.is_achieved else None
        outcome.save()
        return redirect(reverse('outcome_detail', kwargs={'pk': pk}))

    def get(self, request, *args, **kwargs):
        outcome = get_object_or_404(Outcome, pk=self.kwargs['pk'], owner=request.user)
        return render(request, 'set-as-achieved.html', {'outcome': outcome})
