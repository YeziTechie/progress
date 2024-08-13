from django.urls import reverse
from django.views import generic


from abilities.models.outcome import Outcome


class OutcomeDeleteView(generic.DeleteView):
    model = Outcome
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.pk})
