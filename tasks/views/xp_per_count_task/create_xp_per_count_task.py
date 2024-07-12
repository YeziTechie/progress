from django.views.generic.edit import CreateView

from tasks.models.xp_per_count import XpPerCountTask
from tasks.forms.normal_task import CreateTaskForm


class TaskCreateView(CreateView):
    model = NormalTask
    form_class = CreateTaskForm
    template_name = 'create_task.html'
    success_url = '/tasks/list/'

