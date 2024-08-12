from django.views.generic import DetailView

from abilities.models.outcome import Outcome

from tasks.models.classic import Classic
from tasks.models.time import Time
from tasks.models.count import Count
from tasks.models.deadline import Deadline

from user.helpers.generate_level import *


class OutcomeDetailView(DetailView):
    model = Outcome
    template_name = 'retrieve.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        outcome = context['outcome']
        classics = Classic.objects.filter(outcome=outcome)
        times = Time.objects.filter(outcome=outcome)
        counts = Count.objects.filter(outcome=outcome)
        deadlines = Deadline.objects.filter(outcome=outcome)

        outcome.level = calculate_level(outcome.level())

        xp_filled = calculate_xp_for_level(calculate_level()outcome.level()) - calculate_xp_for_level(outcome.level())

        return {
            'xp_filled': xp_filled,
            'xp_remaining': 2,
            'xp_bar_filled': 2,
            'xp_bar_remaining': 2,

            'outcome': outcome,
            'classics': classics,
            'times': times,
            'counts': counts,
            'deadlines': deadlines,
        }
