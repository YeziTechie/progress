from django.views.generic import UpdateView
from django.shortcuts import redirect

from tasks.models.classic_task import ClassicTask
from tasks.forms.classic_task import ClassicTaskUpdateForm


class ClassicTaskUpdateView(UpdateView):
    model = ClassicTask
    form_class = ClassicTaskUpdateForm
    template_name = 'classic_task/update_task.html'

    def form_valid(self, form):
        classic_task = ClassicTask.objects.get(pk=self.kwargs['pk'])
        classic_task.is_done = True
        classic_task.save()
        return redirect('classic_task_detail', pk=classic_task.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classic_task'] = self.object
        return context
