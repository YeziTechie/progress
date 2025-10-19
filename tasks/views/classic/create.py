from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404

from tasks.models.classic import Classic
from tasks.forms.classic import ClassicCreateForm
from outcomes.models.outcome import Outcome


class ClassicCreateView(LoginRequiredMixin, CreateView):
    model = Classic
    form_class = ClassicCreateForm
    template_name = 'classic/create.html'

    def dispatch(self, request, *args, **kwargs):
        # Ensure the user owns the outcome
        self.outcome = get_object_or_404(Outcome, pk=self.kwargs['pk'], owner=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Link task to the outcome
        form.instance.outcome = self.outcome
        # Assign logged-in user as owner of the task
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outcome'] = self.outcome
        return context

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.outcome.pk})
