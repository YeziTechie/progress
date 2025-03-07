from django.views.generic.edit import CreateView
from django.urls import reverse

from outcomes.models.outcome import Outcome
from outcomes.forms.create_outcome import OutcomeCreateForm


class OutcomeCreateView(CreateView):
    model = Outcome
    form_class = OutcomeCreateForm
    template_name = 'create.html'

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.pk})
