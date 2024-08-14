from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from abilities.models.outcome import Outcome

from abilities.models.ecology import InternalEcology
from abilities.forms.questions import InternalEcologyUpdateForm


class InternalEcologyUpdateView(UpdateView):
    model = InternalEcology
    template_name = 'questions/internal-ecology.html'
    context_object_name = 'outcome'
    form_class = InternalEcologyUpdateForm

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk})

    def get_object(self, queryset=None):
        outcome = get_object_or_404(Outcome, pk=self.kwargs['pk'])
        return get_object_or_404(InternalEcology, outcome=outcome)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outcome'] = get_object_or_404(Outcome, pk=self.kwargs['pk'])
        return context
