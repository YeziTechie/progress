from django.views.generic import ListView
from abilities.models.outcome import Outcome
from tasks.models.classic import Classic


class OutcomeListView(ListView):
    model = Outcome
    template_name = 'outcome_list.html'
    context_object_name = 'outcomes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        outcomes = context['outcomes']

        classic_tasks_without_outcome = Classic.objects.filter(outcome__isnull=True)

        for outcome in outcomes:
            classic_tasks = Classic.objects.filter(outcome=outcome)
            outcome.tasks = classic_tasks

        context['classic_without_outcome'] = classic_tasks_without_outcome

        return context
