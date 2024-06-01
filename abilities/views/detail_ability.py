from django.views.generic import DetailView
from abilities.models.ability import Ability
from tasks.models.task import Task


class AbilityDetailView(DetailView):
    model = Ability
    template_name = 'ability_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ability = context['ability']
        tasks = Task.objects.filter(ability=ability)

        
        return {'ability': ability, 'tasks': tasks}