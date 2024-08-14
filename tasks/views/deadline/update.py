from django.views.generic import FormView
from django.shortcuts import get_object_or_404
from django.urls import reverse

from tasks.models.deadline import Deadline
from tasks.forms.deadline import DeadlineUpdateForm


class DeadlineUpdateView(FormView):
    form_class = DeadlineUpdateForm
    template_name = 'deadline/update.html'

    def form_valid(self, form):
        deadline = get_object_or_404(Deadline, pk=self.kwargs['pk'])
        deadline.is_done = True
        deadline.report = form.cleaned_data['report']
        deadline.save()
        return reverse('outcome_detail', kwargs={'pk': deadline.outcome.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Deadline, pk=self.kwargs['pk'])
        context['task'] = task
        return context
