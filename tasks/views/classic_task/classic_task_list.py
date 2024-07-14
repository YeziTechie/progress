from django.views import generic

from tasks.models.classic_task import ClassicTask


class ClassicTaskListView(generic.ListView):
    model = ClassicTask
    template_name = 'classic_task/tasks_list.html'
    context_object_name = 'classic_tasks'
