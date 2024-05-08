from django.views.generic.edit import CreateView
from abilities.models.ability import Ability
from abilities.forms.create_ability import CreateAbilityForm


class AbilityCreateView(CreateView):
    model = Ability
    form_class = CreateAbilityForm
    template_name = 'create_ability.html'
    success_url = '/abilities/list/'

