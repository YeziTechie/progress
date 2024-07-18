from django.views.generic import FormView
from django.shortcuts import redirect, get_object_or_404

from tasks.models.deadline import Deadline
from tasks.forms.deadline import DeadlineAbortForm


class DeadlineAbortView(FormView):
    form_class = DeadlineAbortForm
    template_name = 'deadline/Abort.html'
    success_url = '/'

    def form_valid(self, form):
        deadline = get_object_or_404(Deadline, pk=self.kwargs['pk'])
        deadline.is_aborted = True
        deadline.save()
        return redirect('outcome_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        deadline = get_object_or_404(Deadline, pk=self.kwargs['pk'])
        context['deadline'] = deadline
        return context
