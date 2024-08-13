from django.urls import reverse
from django.views.generic import DeleteView

from tasks.models.classic import Classic


class ClassicDeleteView(DeleteView):
    model = Classic
    context_object_name = 'task'
    template_name = 'classic/delete.html'

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk})
