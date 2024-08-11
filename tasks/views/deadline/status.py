from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from tasks.models.deadline import Deadline


class DeadlineStatus(TemplateView):
    template_name = 'deadline/status.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = get_object_or_404(Deadline, pk=self.kwargs['pk'])
        context['obj'] = obj
        return context
