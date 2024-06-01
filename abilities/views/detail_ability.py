from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import DetailView
from abilities.models.ability import Ability
from tasks.models.task import Task


class AbilityDetailView(DetailView):
    model = Ability
    template_name = 'ability-detail.html'

    def get_context_data(self, **kwargs):
        ability = super().get_context_data(**kwargs)
        tasks = Task.objects.all(abiilty=ability)
        
        return ability, tasks