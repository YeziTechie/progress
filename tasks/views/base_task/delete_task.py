from django.views import generic
from tasks.models.normal_task import NormalTask


class TaskDeleteView(generic.DeleteView):
    model = NormalTask
    template_name = 'delete_task.html'
    success_url = '/tasks/list/'
