from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone

from tasks.models.deadline import Deadline
from tasks.forms.deadline import DeadlineRepeatForm, DeadlineUpdateForm


class DeadlineStatus(LoginRequiredMixin, TemplateView):
    template_name = 'deadline/status.html'

    def get_deadline(self):
        return get_object_or_404(Deadline, pk=self.kwargs['pk'], outcome__owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_deadline()

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