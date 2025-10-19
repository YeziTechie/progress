from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from tasks.models.deadline import Deadline
from tasks.forms.deadline import DeadlineRepeatForm


class DeadlineRepeatView(LoginRequiredMixin, FormView):
    template_name = 'deadline/repeat.html'
    form_class = DeadlineRepeatForm

    def get_deadline(self):
        return get_object_or_404(
            Deadline,
            pk=self.kwargs['pk'],
            outcome__owner=self.request.user
        )

    def dispatch(self, request, *args, **kwargs):
        """Redirect early if the deadline is not over yet."""
        obj = self.get_deadline()
        if not obj.is_time_over():
            messages.error(
                request,
                'The duration of this task is not over yet. You still have time.'.title()
            )
            return redirect('deadline_status', pk=obj.pk)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = self.get_deadline()
        date = form.cleaned_data.get('deadline_date')
        obj.deadline_date = date
        obj.penalty_xp += obj.xp * obj.penalty
        obj.save()
        messages.success(self.request, 'Deadline successfully extended.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.get_deadline().outcome.pk})

    def get_context_data(self, **kwargs):
        """Only adds context — never redirects."""
        context = super().get_context_data(**kwargs)
        context['task'] = self.get_deadline()
        return context
