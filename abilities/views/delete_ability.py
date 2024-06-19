from django.views import generic
from abilities.models.outcome import Outcome


class AbilityDeleteView(generic.DeleteView):
    model = Outcome
    template_name = 'ability_confirm_delete.html'
    success_url = '/abilities/list/'
