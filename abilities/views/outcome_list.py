from django.views import generic
from datetime import datetime
from abilities.models.outcome import Outcome
from tasks.models.classic_task import ClassicTask


class OutcomeListGenericView(generic.ListView):
    model = Outcome
    template_name = 'outcome_list.html'
    context_object_name = 'outcomes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        outcomes = context['outcomes']
        print(datetime.now('tehran'))

        classic_tasks_without_outcome = ClassicTask.objects.filter(outcome__isnull=True)

        for outcome in outcomes:
            classic_tasks = ClassicTask.objects.filter(outcome=outcome)
            outcome.tasks = classic_tasks

        context['classic_tasks_without_outcome'] = classic_tasks_without_outcome

        return context
