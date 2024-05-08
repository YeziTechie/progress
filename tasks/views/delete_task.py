from django.views import generic
from tasks.models.task import Task


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = '/tasks/list/'
