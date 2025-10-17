from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.views.generic import FormView

from tasks.models.time import Time
from tasks.forms.time import TimeCreateForm, TimeUpdateForm
from outcomes.models.outcome import Outcome


class TimeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Time
    context_object_name = 'task'
    template_name = 'time/delete.html'
    login_url = 'login'

    def get_queryset(self):
        # Restrict deletion to tasks owned by the current user
        return Time.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk})

