from django.views.generic import DetailView
from abilities.models.outcome import Outcome
from tasks.models.task import Task


class OutcomeDetailView(DetailView):
    model = Outcome
    template_name = 'outcome_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        outcome = context['outcome']
        tasks = Task.objects.filter(outcome=outcome)

        return {'outcome': outcome, 'tasks': tasks}
