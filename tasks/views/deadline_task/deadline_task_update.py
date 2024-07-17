from django.views.generic import FormView
from django.shortcuts import redirect, get_object_or_404

from tasks.models.time_task import TimeTask
from tasks.forms.time_task import TimeTaskUpdateForm


class TimeTaskUpdateView(FormView):
    form_class = TimeTaskUpdateForm
    template_name = 'time_task/update_task.html'

    def form_valid(self, form):
        time = int(form.cleaned_data['time'])
        if time > 0:
            time_task = get_object_or_404(TimeTask, pk=self.kwargs['pk'])
            time_task.total_time += time
            time_task.save()

        return redirect('outcome_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_task'] = get_object_or_404(TimeTask, pk=self.kwargs['pk'])
        return context
