from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse

from outcomes.models.outcome import Outcome
from outcomes.models.questions import OutcomeQuestions
from outcomes.forms.questions import OutcomeQuestionsUpdateForm


class OutcomeQuestionsUpdateView(LoginRequiredMixin, UpdateView):
    model = OutcomeQuestions
    template_name = 'questions/outcome-questions.html'
    context_object_name = 'outcome'
    form_class = OutcomeQuestionsUpdateForm
    login_url = 'login'

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk})

    def get_object(self, queryset=None):
        outcome = get_object_or_404(Outcome, pk=self.kwargs['pk'])
        return get_object_or_404(OutcomeQuestions, outcome=outcome)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outcome'] = get_object_or_404(Outcome, pk=self.kwargs['pk'])
        return context
