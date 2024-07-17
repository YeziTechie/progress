from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from tasks.models.deadline_task import DeadlineTask


class DeadlineTaskStatus(TemplateView):
    template_name = 'deadline_task/status.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(DeadlineTask, pk=self.kwargs['pk'])
        context['task'] = task
        return context
