from django.views import generic

from abilities.models.outcome import Outcome
from tasks.models.task import Task


class OutcomeListGenericView(generic.ListView):
    model = Outcome
    template_name = 'outcome_list.html'
    context_object_name = 'abilities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        outcomes = context['abilities']

        # Fetch tasks that do not have an associated ability
        tasks_without_outcome = Task.objects.filter(outcome__isnull=True)

        # Iterate through each ability and fetch related tasks
        for outcome in outcomes:
            tasks = Task.objects.filter(outcome=outcome)
            outcome.tasks = tasks  # Add tasks to ability object

        # Add tasks without an associated ability to context
        context['tasks_without_outcome'] = tasks_without_outcome

        return context
