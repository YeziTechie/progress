from django.views import generic
from django.urls import reverse

from tasks.models.deadline import Deadline


class DeadlineDeleteView(generic.DeleteView):
    model = Deadline
    context_object_name = 'task'
    template_name = 'deadline/delete.html'

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk})
