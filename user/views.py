from django.shortcuts import render
from django.views import View

from abilities.models.outcome import Outcome

from tasks.models.deadline import Deadline
from tasks.models.classic import Classic

from .helpers.status import total_xp, outcome_total_tasks_undone, count_scored, time_spent
from .helpers.generate_level import calculate_level, calculate_xp_for_level


class UserProfileView(View):
    '''
        deadline done 1
        classic done 1
        time spent 1
        count scored 1

        last outcome created 1
        total outcomes 1
        last outcome achieved 1

        highest xp by single task 1
        last task done 1
        total xp lost
    '''

    def get(self, request, *args, **kwargs):

        # xp and level, next level and current xp and stuff
        xp = total_xp()
        level = calculate_level(xp=xp)
        next_level_xp = calculate_xp_for_level(calculate_level(xp=xp) + 1)
        xp = xp - calculate_xp_for_level(level)
        next_level_xp = next_level_xp - calculate_xp_for_level(level)

        # Percentate for width of the design property
        num1 = xp
        num2 = next_level_xp - xp
        per1 = round((num1 / next_level_xp) * 100)
        per2 = round((num2 / next_level_xp) * 100)

        outcomes = Outcome.objects.all()
        res = []


        # highest xp
        highest_xp = 0

        classic_high = Classic.objects.order_by('-xp').first()
        deadline_high = Deadline.objects.order_by('-xp').first()

        if deadline_high.xp < classic_high.xp:
            highest_xp = classic_high.xp
        else:
            highest_xp = deadline_high.xp

        # last task done
        last_task_done = None

        classic_done = Classic.objects.order_by('-done_at').first()
        deadline_done = Deadline.objects.order_by('-done_at').first()

        if deadline_done.done_at < classic_done.done_at:
            last_task_done = deadline_done.done_at
        else:
            last_task_done = classic_done.done_at



        for outcome in outcomes:
            output = {
                "pk": outcome.pk,
                "name": outcome.name,
                "total_tasks_undone": outcome_total_tasks_undone(outcome.pk),
            }

            res.append(output)

        context = {
            "total_xp": xp,
            "level": calculate_level(xp=xp),
            "next_level_xp": next_level_xp,

            "filled": per1,
            "remaining": per2,

            "classic_done": len(Classic.objects.filter(is_done=True)),
            "deadline_done": len(Deadline.objects.filter(is_done=True)),
            "count_scored": count_scored(),
            "time_spent": time_spent(),

            "outcomes": res,
            "total_outcomes": len(Outcome.objects.all()),
            "last_created_outcome": Outcome.objects.order_by('-created_at').first(),
            "last_created_achieved": Outcome.objects.order_by('-achieved_at').first(),

            "highest_xp_by_single_task": highest_xp,
            "last_task_done": last_task_done,
        }

        return render(request, 'profile.html', context)
