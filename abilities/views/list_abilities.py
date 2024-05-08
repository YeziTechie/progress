from django.views import generic

from abilities.models.ability import Ability
from tasks.models.task import Task


class AbilityListGenericView(generic.ListView):
    model = Ability
    template_name = 'all_abilities.html'
    context_object_name = 'abilities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        abilities = context['abilities']

        # Fetch tasks that do not have an associated ability
        tasks_without_ability = Task.objects.filter(ability__isnull=True)

        # Iterate through each ability and fetch related tasks
        for ability in abilities:
            tasks = Task.objects.filter(ability=ability)
            ability.tasks = tasks  # Add tasks to ability object

        # Add tasks without an associated ability to context
        context['tasks_without_ability'] = tasks_without_ability

        return context