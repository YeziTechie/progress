from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, DeleteView
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from outcomes.models.outcome import Outcome
from tasks.models.deadline import Deadline
from tasks.forms.deadline import DeadlineCreateForm


class DeadlineAbortView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        deadline = get_object_or_404(Deadline, pk=self.kwargs['pk'], outcome__owner=request.user)
        if not deadline.is_aborted:
            deadline.is_aborted = True
            deadline.penalty_xp += deadline.xp * deadline.penalty
            deadline.save()
            return redirect(reverse('outcome_detail', kwargs={'pk': deadline.outcome.pk}))
        else:
            raise Exception("This task is already aborted")

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Deadline, pk=self.kwargs['pk'], outcome__owner=request.user)
        return render(request, 'deadline/abort.html', {'task': task})

