from django.views.generic.edit import CreateView
from tasks.models.task import Task
from tasks.forms.create_task import CreateTaskForm


class TaskCreateView(CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'create_task.html'
    success_url = '/tasks/list/'

