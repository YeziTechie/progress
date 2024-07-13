from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from tasks.models.classic_task import ClassicTask
from tasks.forms.classic_task import ClassicTaskUpdateForm


class ClassicTaskUpdateView(FormView):
    template_name = 'classic_task/update_task.html'
    form_class = ClassicTaskUpdateForm

    def form_valid(self, form):
        classic_task = ClassicTask.objects.get(pk=self.kwargs['pk'])
        classic_task.is_done = True
        classic_task.save()
        return redirect('classic_task_detail', pk=classic_task.pk)

    def get_success_url(self):
        return reverse_lazy('classic_task_detail', kwargs={'pk': self.kwargs['pk']})
