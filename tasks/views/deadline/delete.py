from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse

from tasks.models.deadline import Deadline


class DeadlineDeleteView(LoginRequiredMixin, DeleteView):
    model = Deadline
    context_object_name = 'task'
    template_name = 'deadline/delete.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.outcome.owner != self.request.user:
            raise PermissionError("You do not have permission to delete this task.")
        return obj

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk})
