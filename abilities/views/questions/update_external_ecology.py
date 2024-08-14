from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from abilities.models.outcome import Outcome

from abilities.models.ecology import ExternalEcology
from abilities.forms.questions import ExternalEcologyUpdateForm


class ExternalEcologyUpdateView(UpdateView):
    model = ExternalEcology
    template_name = 'questions/external-ecology.html'
    context_object_name = 'outcome'
    form_class = ExternalEcologyUpdateForm

    def get_success_url(self):
        return redirect(reverse('outcome_detail', kwargs={'pk': self.object.pk}))

    def get_object(self, queryset=None):
        outcome = get_object_or_404(Outcome, pk=self.kwargs['pk'])
        return get_object_or_404(ExternalEcology, outcome=outcome)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outcome'] = get_object_or_404(Outcome, pk=self.kwargs['pk'])
        return context
