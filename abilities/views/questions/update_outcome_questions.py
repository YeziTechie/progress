from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse

from abilities.models.outcome import Outcome

from abilities.models.questions import OutcomeQuestions
from abilities.forms.questions import OutcomeQuestionsUpdateForm


class OutcomeQuestionsUpdateView(UpdateView):
    model = OutcomeQuestions
    template_name = 'questions/outcome-questions.html'
    context_object_name = 'outcome'
    form_class = OutcomeQuestionsUpdateForm

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        outcome = get_object_or_404(Outcome, pk=self.kwargs['pk'])
        return get_object_or_404(OutcomeQuestions, outcome=outcome)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outcome'] = get_object_or_404(Outcome, pk=self.kwargs['pk'])
        return context
