from django.views.generic import DetailView
from tasks.models.classic_task import ClassicTask


class ClassicTaskDetailView(DetailView):
    model = ClassicTask
    context_object_name = 'classic_task'
    template_name = 'classic_task/task_detail.html'
