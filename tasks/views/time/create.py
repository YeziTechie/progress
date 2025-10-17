from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.views.generic import FormView

from tasks.models.time import Time
from tasks.forms.time import TimeCreateForm, TimeUpdateForm
from outcomes.models.outcome import Outcome


class TimeCreateView(LoginRequiredMixin, CreateView):
    model = Time
    form_class = TimeCreateForm
    template_name = 'time/create.html'
    login_url = 'login'

    def form_valid(self, form):
        # Assign the outcome and the logged-in user as owner
        form.instance.outcome = get_object_or_404(Outcome, pk=self.kwargs['pk'])
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outcome'] = get_object_or_404(Outcome, pk=self.kwargs['pk'])
        return context

