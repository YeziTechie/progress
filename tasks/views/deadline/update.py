from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone

from tasks.models.deadline import Deadline
from tasks.forms.deadline import DeadlineRepeatForm, DeadlineUpdateForm


class DeadlineUpdateView(LoginRequiredMixin, FormView):
    form_class = DeadlineUpdateForm
    template_name = 'deadline/update.html'

    def get_deadline(self):
        return get_object_or_404(Deadline, pk=self.kwargs['pk'], outcome__owner=self.request.user)

    def form_valid(self, form):
        deadline = self.get_deadline()
        deadline.is_done = True
        deadline.report = form.cleaned_data['report']
        deadline.save()
        return redirect(reverse('outcome_detail', kwargs={'pk': deadline.outcome.pk}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.get_deadline()
        return context