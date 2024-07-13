from django.views.generic.edit import CreateView
from abilities.models.outcome import Outcome
from abilities.forms.create_outcome import CreateOutcomeForm


class OutcomeCreateView(CreateView):
    model = Outcome
    form_class = CreateOutcomeForm
    template_name = 'create_outcome.html'
    success_url = '/outcomes/list/'

