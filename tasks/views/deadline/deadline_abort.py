from django.views.generic import FormView
from django.views import View
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse

from tasks.models.deadline import Deadline


class DeadlineAbortView(View):
    def post(self, request, *args, **kwargs):
        deadline = get_object_or_404(Deadline, pk=self.kwargs['pk'])
        if deadline.is_aborted is False:
            deadline.is_aborted = True
            deadline.penalty_xp += deadline.xp * deadline.penalty
            deadline.save()
            return redirect(reverse('outcome_list'))
        else:
            raise Exception("this task is already aborted".title())

    def get(self, request, *args, **kwargs):
        deadline = get_object_or_404(Deadline, pk=self.kwargs['pk'])
        return render(request, 'deadline/abort.html', {'deadline': deadline})
