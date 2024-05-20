from django.shortcuts import render
from django.views import View

# from tasks.models.task import Task
from abilities.models.ability import Ability

from .helpers.total_xp import total_xp
from .helpers.total_tasks_done import total_tasks_done
from .helpers.generate_level import calculate_level, calculate_xp_for_level
from .helpers.total_outcome_tasks_undone import outcome_total_tasks_undone
from .helpers.total_outcome_tasks_done import outcome_total_tasks_done


class UserProfileView(View):
    def get(self, request, *args, **kwargs):

        xp = total_xp()
        level = calculate_level(xp=xp)
        next_level_xp = calculate_xp_for_level(calculate_level(xp=xp) + 1)

        abilities = Ability.objects.all()
        outcomes = []

        for ability in abilities:
            outcome = {
                "name": ability.name,
                "level": calculate_level(ability.total_xp),
                "total_tasks_done": outcome_total_tasks_done(ability.pk),
                "total_tasks_undone": outcome_total_tasks_undone(ability.pk),
            }

            outcomes.append(outcome)

        context = {
            "total_xp": total_xp,
            "level": level,
            "next_level_xp": next_level_xp,
            "total_tasks_done": total_tasks_done(),
            "outcomes": outcomes
        }

        return render(request, 'profile.html', context)

