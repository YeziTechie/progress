from django.views.generic import DetailView
from abilities.models.outcome import Outcome
from tasks.models.classic_task import ClassicTask


class OutcomeDetailView(DetailView):
    model = Outcome
    template_name = 'outcome_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        outcome = context['outcome']
        classic_tasks = ClassicTask.objects.filter(outcome=outcome)

        return {'outcome': outcome, 'classic_tasks': classic_tasks}
