from django.views.generic.edit import CreateView
from tasks.models.normal_task import NormalTask
from tasks.forms.create_task import CreateTaskForm


class TaskCreateView(CreateView):
    model = NormalTask
    form_class = CreateTaskForm
    template_name = 'create_task.html'
    success_url = '/tasks/list/'

