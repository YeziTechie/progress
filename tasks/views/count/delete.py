from django.views import generic
from django.urls import reverse
from django.shortcuts import redirect

from tasks.models.count import Count


class CountDeleteView(generic.DeleteView):
    model = Count
    context_object_name = 'task'
    template_name = 'count/delete.html'

    def get_success_url(self):
        return redirect(reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk}))

