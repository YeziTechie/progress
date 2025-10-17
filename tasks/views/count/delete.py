from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.shortcuts import get_object_or_404
from django.urls import reverse

from outcomes.models.outcome import Outcome
from tasks.models.count import Count
from tasks.forms.count import CountCreateForm, CountUpdateForm


class CountDeleteView(LoginRequiredMixin, DeleteView):
    model = Count
    context_object_name = 'task'
    template_name = 'count/delete.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.outcome.owner != self.request.user:
            raise PermissionError("You do not have permission to delete this task.")
        return obj

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk})

