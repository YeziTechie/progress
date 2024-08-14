from django.views import generic
from django.urls import reverse
from django.shortcuts import redirect

from tasks.models.deadline import Deadline


class DeadlineDeleteView(generic.DeleteView):
    model = Deadline
    context_object_name = 'task'
    template_name = 'deadline/delete.html'

    def get_success_url(self):
        return redirect(reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk}))
