from django.views import generic
from abilities.models.outcome import Outcome


class AbilityDeleteView(generic.DeleteView):
    model = Outcome
    template_name = 'delete_outcome.html'
    success_url = '/abilities/list/'
