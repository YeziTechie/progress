from django.views.generic.edit import CreateView
from abilities.models.outcome import Outcome
from abilities.forms.create_ability import CreateAbilityForm


class AbilityCreateView(CreateView):
    model = Outcome
    form_class = CreateAbilityForm
    template_name = 'create_ability.html'
    success_url = '/abilities/list/'

