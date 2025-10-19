from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse

from outcomes.models.outcome import Outcome
from tasks.models.deadline import Deadline
from tasks.forms.deadline import DeadlineCreateForm


class DeadlineCreateView(LoginRequiredMixin, CreateView):
    model = Deadline
    form_class = DeadlineCreateForm
    template_name = 'deadline/create.html'

    def dispatch(self, request, *args, **kwargs):
        # Ensure the user owns the outcome
        self.outcome = get_object_or_404(Outcome, pk=self.kwargs['pk'], owner=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.outcome = self.outcome
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outcome'] = self.outcome
        return context

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.outcome.pk})
