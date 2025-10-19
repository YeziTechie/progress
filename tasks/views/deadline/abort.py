from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from tasks.models.deadline import Deadline


class DeadlineAbortView(LoginRequiredMixin, View):
    """Allows the user to abort a deadline safely, with messages and redirects."""

    def dispatch(self, request, *args, **kwargs):
        """Redirect early if the deadline is already aborted."""
        deadline = get_object_or_404(Deadline, pk=kwargs['pk'], outcome__owner=request.user)
        if deadline.is_aborted:
            messages.error(request, "This task has already been aborted.")
            return redirect('deadline_status', pk=deadline.pk)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Handle form submission to abort the deadline."""
        deadline = get_object_or_404(Deadline, pk=self.kwargs['pk'], outcome__owner=request.user)

        # Mark as aborted and apply penalty XP
        deadline.is_aborted = True
        deadline.penalty_xp += deadline.xp * deadline.penalty
        deadline.save()

        messages.success(request, "The task was successfully aborted.")
        return redirect('outcome_detail', pk=deadline.outcome.pk)

    def get(self, request, *args, **kwargs):
        """Render the confirmation page to abort the deadline."""
        task = get_object_or_404(Deadline, pk=self.kwargs['pk'], outcome__owner=request.user)
        return render(request, 'deadline/abort.html', {'task': task})
