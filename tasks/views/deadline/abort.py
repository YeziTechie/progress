from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from tasks.models.deadline import Deadline


class DeadlineAbortView(View):
    def post(self, request, *args, **kwargs):
        deadline = get_object_or_404(Deadline, pk=self.kwargs['pk'])
        if deadline.is_aborted is False:
            deadline.is_aborted = True
            deadline.penalty_xp += deadline.xp * deadline.penalty
            deadline.save()
            return redirect(reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk}))
        else:
            raise Exception("this task is already aborted".title())

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Deadline, pk=self.kwargs['pk'])
        return render(request, 'deadline/abort.html', {'task': task})

