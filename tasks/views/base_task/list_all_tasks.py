from django.views import generic

from tasks.models.task import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = 'tasks_list.html'
    context_object_name = 'tasks'

