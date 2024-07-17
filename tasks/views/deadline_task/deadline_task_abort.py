from django.views.generic import FormView
from django.shortcuts import redirect, get_object_or_404

from tasks.models.deadline_task import DeadlineTask
from tasks.forms.deadline_task import DeadlineTaskAbortForm


class DeadlineTaskAbortView(FormView):
    form_class = DeadlineTaskAbortForm
    template_name = 'deadline_task/Abort.html'
    success_url = '/'

    def form_valid(self, form):
        task = get_object_or_404(DeadlineTask, pk=self.kwargs['pk'])
        task.is_aborted = True
        task.save()
        return redirect('outcome_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(DeadlineTask, pk=self.kwargs['pk'])
        context['task'] = task
        return context

