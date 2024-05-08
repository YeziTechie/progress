from django.views import generic
from abilities.models.ability import Ability


class AbilityDeleteView(generic.DeleteView):
    model = Ability
    template_name = 'ability_confirm_delete.html'
    success_url = '/abilities/list/'
