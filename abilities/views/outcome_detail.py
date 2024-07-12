from django.views.generic import DetailView
from abilities.models.outcome import Outcome
from tasks.models.normal_task import NormalTask


class OutcomeDetailView(DetailView):
    model = Outcome
    template_name = 'outcome_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        outcome = context['outcome']
        tasks = NormalTask.objects.filter(outcome=outcome)

        return {'outcome': outcome, 'tasks': tasks}
