from django.views.generic import DetailView
from abilities.models.outcome import Outcome
from tasks.models.classic import Classic


class OutcomeDetailView(DetailView):
    model = Outcome
    template_name = 'outcome_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        outcome = context['outcome']
        classics = Classic.objects.filter(outcome=outcome)

        return {'outcome': outcome, 'classics': classics}
