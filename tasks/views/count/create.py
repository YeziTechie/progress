from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404

from tasks.models.count import Count
from tasks.forms.count import CountCreateForm
from outcomes.models.outcome import Outcome


class CountCreateView(LoginRequiredMixin, CreateView):
    model = Count
    form_class = CountCreateForm
    template_name = 'count/create.html'
    login_url = 'login'

    def form_valid(self, form):
        # Assign outcome based on URL pk
        form.instance.outcome = get_object_or_404(Outcome, pk=self.kwargs['pk'])
        # Assign logged-in user as owner
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outcome'] = get_object_or_404(Outcome, pk=self.kwargs['pk'])
        return context
