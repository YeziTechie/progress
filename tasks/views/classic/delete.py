from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect

from tasks.models.classic import Classic
from tasks.forms.classic import ClassicCreateForm, ClassicUpdateForm
from outcomes.models.outcome import Outcome


class ClassicDeleteView(LoginRequiredMixin, DeleteView):
    model = Classic
    template_name = 'classic/delete.html'
    context_object_name = 'task'

    def get_object(self, queryset=None):
        # Only allow deletion if the user owns the outcome linked to the task
        obj = super().get_object(queryset)
        if obj.outcome.owner != self.request.user:
            raise PermissionError("You do not have permission to delete this task.")
        return obj

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk})