from django.utils import timezone
from django.views.generic import DetailView

from abilities.models.outcome import Outcome

from user.helpers.generate_level import *
from user.helpers.status import outcome_active_tasks


class OutcomeDetailView(DetailView):
    model = Outcome
    template_name = 'retrieve.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        outcome = context['outcome']

        # task objects
        classics = outcome.classic_tasks.all()
        times = outcome.time_tasks.all()
        counts = outcome.count_tasks.all()
        deadlines = outcome.deadline_tasks.all()

        for i in deadlines:
            i.penalty = round(i.penalty * i.xp)
            i.failed = round(i.penalty_xp / i.xp)

            now = timezone.now()
            time_diff = i.deadline_date - now

            days = time_diff.days
            hours, remainder = divmod(time_diff.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            i.days = days
            i.hours = hours
            i.minutes = minutes


        # question objects
        internal_ecology = outcome.internal_ecology
        questions = outcome.outcome_questions
        external_ecology = outcome.external_ecology

        # level and xp stuff
        level = calculate_level(outcome.total_xp())

        total_xp = outcome.total_xp()
        current_xp = total_xp - calculate_xp_for_level(level)
        required_xp = calculate_xp_for_level(level + 1) - calculate_xp_for_level(level)

        per1 = round((current_xp / required_xp) * 100) if required_xp != 0 else 0
        per2 = 100 - per1

        return {
            'level': level,
            'current_xp': current_xp,
            'required_xp': required_xp,
            'per1': per1,
            'per2': per2,

            'active_tasks': outcome_active_tasks(outcome.pk),
            'done_tasks': len(classics.filter(is_done=True)) + len(deadlines.filter(is_done=True)),

            'outcome': outcome,

            'internal_ecology': internal_ecology,
            'outcome_questions': questions,
            'external_ecology': external_ecology,

            'classics': classics,
            'times': times,
            'counts': counts,
            'deadlines': deadlines,
        }
