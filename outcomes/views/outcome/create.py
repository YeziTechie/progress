from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse

from outcomes.models.outcome import Outcome
from outcomes.forms.create_outcome import OutcomeCreateForm


class OutcomeCreateView(LoginRequiredMixin, CreateView):
    model = Outcome
    form_class = OutcomeCreateForm
    template_name = 'create.html'
    login_url = 'login'  # redirect if not logged in

    def form_valid(self, form):
        # Attach the logged-in user to the 'owner' field before saving
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.pk})
