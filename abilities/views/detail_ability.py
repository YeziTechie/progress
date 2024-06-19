from django.views.generic import DetailView
from abilities.models.outcome import Outcome
from tasks.models.task import Task


class AbilityDetailView(DetailView):
    model = Outcome
    template_name = 'outcome_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ability = context['ability']
        tasks = Task.objects.filter(ability=ability)

        
        return {'ability': ability, 'tasks': tasks}