from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone

from tasks.models.deadline import Deadline
from tasks.forms.deadline import DeadlineRepeatForm, DeadlineUpdateForm


class DeadlineRepeatView(LoginRequiredMixin, FormView):
    template_name = 'deadline/repeat.html'
    form_class = DeadlineRepeatForm

    def get_deadline(self):
        return get_object_or_404(Deadline, pk=self.kwargs['pk'], outcome__owner=self.request.user)

    def form_valid(self, form):
        obj = self.get_deadline()
        if obj.is_time_over():
            date = form.cleaned_data.get('deadline_date')
            obj.deadline_date = date
            obj.penalty_xp += obj.xp * obj.penalty
            obj.save()
            return super().form_valid(form)
        else:
            raise Exception('The duration of this task is not over yet. You still have time.'.title())

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.get_deadline().outcome.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_deadline()
        if not task.is_time_over():
            raise Exception('The duration of this task is not over yet. You still have time.'.title())
        context['task'] = task
        return context
