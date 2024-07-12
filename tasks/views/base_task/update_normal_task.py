from tasks.models.normal_task import NormalTask

from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from tasks.forms.normal_task import TaskUpdateForm


class TaskUpdateView(FormView):
    template_name = 'normal_task/update_task.html'
    form_class = TaskUpdateForm

    def form_valid(self, form):
        task = NormalTask.objects.get(pk=self.kwargs['pk'])
        task.is_done = True
        task.save()
        return redirect('task_detail', pk=task.pk)

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.kwargs['pk']})
