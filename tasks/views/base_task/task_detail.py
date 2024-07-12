from django.views.generic import DetailView
from tasks.models.normal_task import NormalTask


class TaskDetailView(DetailView):
    model = NormalTask
    template_name = 'task_detail.html'
    context_object_name = 'task'
