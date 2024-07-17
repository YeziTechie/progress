from django.views.generic.edit import CreateView

from tasks.models.deadline_task import DeadlineTask
from tasks.forms.deadline_task import DeadlineTaskCreateForm


class DeadlineTaskCreateView(CreateView):
    model = DeadlineTask
    form_class = DeadlineTaskCreateForm
    template_name = 'deadline_task/create_task.html'
    success_url = '/'
