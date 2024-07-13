from django.views import generic

from abilities.models.outcome import Outcome
from tasks.models.normal_task import NormalTask


class OutcomeListGenericView(generic.ListView):
    model = Outcome
    template_name = 'outcome_list.html'
    context_object_name = 'outcomes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        outcomes = context['outcomes']

        tasks_without_outcome = NormalTask.objects.filter(outcome__isnull=True)

        for outcome in outcomes:
            tasks = NormalTask.objects.filter(outcome=outcome)
            outcome.tasks = tasks

        context['normal task_without_outcome'] = tasks_without_outcome

        return context
