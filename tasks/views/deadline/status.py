from django.utils import timezone
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from tasks.models.deadline import Deadline


class DeadlineStatus(TemplateView):
    template_name = 'deadline/status.html'

    def get_success_url(self):
        return redirect(reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Deadline, pk=self.kwargs['pk'])

        now = timezone.now()
        time_diff = task.deadline_date - now

        days = time_diff.days
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        task.days = days
        task.hours = hours
        task.minutes = minutes

        context['task'] = task

        return context
