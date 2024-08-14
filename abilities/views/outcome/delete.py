from django.urls import reverse
from django.views.generic import DeleteView

from abilities.models.outcome import Outcome


class OutcomeDeleteView(DeleteView):
    model = Outcome
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse('profile')
