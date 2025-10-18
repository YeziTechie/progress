from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DeleteView
from django.shortcuts import get_object_or_404

from outcomes.models.outcome import Outcome


class OutcomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Outcome
    template_name = 'delete.html'
    login_url = 'login'

    def get_object(self, queryset=None):
        # Only allow deleting outcomes that belong to the current user
        return get_object_or_404(Outcome, pk=self.kwargs['pk'], owner=self.request.user)

    def get_success_url(self):
        return reverse('profile')
