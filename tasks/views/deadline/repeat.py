from django.views.generic import FormView
from django.shortcuts import get_object_or_404
from django.urls import reverse

from tasks.models.deadline import Deadline
from tasks.forms.deadline import DeadlineRepeatForm


class DeadlineRepeatView(FormView):
    template_name = 'deadline/repeat.html'
    form_class = DeadlineRepeatForm

    def form_valid(self, form):
        obj = get_object_or_404(Deadline, pk=self.kwargs['pk'])
        if obj.is_time_over():
            date = form.cleaned_data.get('deadline_date')
            obj.deadline_date = date
            obj.penalty_xp += obj.xp * obj.penalty
            obj.save()
            return reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk})
        else:
            raise Exception('The duration of this task is not over yet. You still have time.'.title())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Deadline, pk=self.kwargs['pk'])

        if not task.is_time_over():
            raise Exception('The duration of this task is not over yet. You still have time.'.title())
        context['task'] = task
        return context
