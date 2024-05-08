from django.views import generic

from tasks.models.task import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = 'all_tasks.html'
    context_object_name = 'tasks'

