from django.views import generic
from django.urls import reverse

from tasks.models.time import Time


class TimeDeleteView(generic.DeleteView):
    model = Time
    context_object_name = 'task'
    template_name = 'time/delete.html'

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk})
