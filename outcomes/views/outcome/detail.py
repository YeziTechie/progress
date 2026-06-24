from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import DetailView
from django.contrib import messages
from django.shortcuts import get_object_or_404

from outcomes.models.outcome import Outcome
from user.helpers.generate_level import calculate_level, calculate_xp_for_level


class OutcomeDetailView(LoginRequiredMixin, DetailView):
    model = Outcome
    template_name = 'retrieve.html'
    login_url = 'login'  # redirect if not logged in

    def get_object(self, queryset=None):
        # Ensure only the owner can access this outcome
        return get_object_or_404(Outcome, pk=self.kwargs['pk'], owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        outcome = context['outcome']

        # Task objects
        classics = outcome.classic_tasks.order_by('is_done')
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

        # Question objects
        internal_ecology = outcome.internal_ecology
        questions = outcome.outcome_questions
        external_ecology = outcome.external_ecology

        # Level and XP calculations
        level = calculate_level(outcome.total_xp())
        if level > 0:
            xp = outcome.total_xp() - calculate_xp_for_level(level)
            next_level_xp = calculate_xp_for_level(level + 1) - calculate_xp_for_level(level)
        else:
            xp = outcome.total_xp()
            next_level_xp = 100

        per1 = round((xp / next_level_xp) * 100) if next_level_xp != 0 else 0
        per2 = 100 - per1

        a = 2
        b = 5
        c = b + a

        context.update({
            'current_xp': xp,
            'required_xp': next_level_xp,
            'per1': per1,
            'per2': per2,
            'internal_ecology': internal_ecology,
            'outcome_questions': questions,
            'external_ecology': external_ecology,
            'classics': classics,
            'times': times,
            'counts': counts,
            'deadlines': deadlines,
            'done_tasks': len(classics.filter(is_done=True)) + len(deadlines.filter(is_done=True)),
        })

        messages.info(self.request, 'Everything is possible. Act..!')

        return context

