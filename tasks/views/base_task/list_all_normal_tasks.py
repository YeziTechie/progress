from django.views import generic

from tasks.models.normal_task import NormalTask


class TaskListView(generic.ListView):
    model = NormalTask
    template_name = 'normal_task/tasks_list.html'
    context_object_name = 'tasks'

