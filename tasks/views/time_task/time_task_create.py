from django.views.generic.edit import CreateView

from tasks.models.time_task import TimeTask
from tasks.forms.time_task import TimeTaskCreateForm


class TimeTaskCreateView(CreateView):
    model = TimeTask
    form_class = TimeTaskCreateForm
    template_name = 'time_task/create_task.html'
    success_url = '/'
