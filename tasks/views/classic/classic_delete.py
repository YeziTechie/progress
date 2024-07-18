from django.views import generic
from tasks.models.classic_task import ClassicTask


class ClassicTaskDeleteView(generic.DeleteView):
    model = ClassicTask
    context_object_name = 'classic_task'
    template_name = 'classic_task/delete_task.html'
    success_url = ''
