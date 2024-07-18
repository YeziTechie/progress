from django.views.generic.edit import CreateView

from tasks.models.deadline import Deadline
from tasks.forms.deadline import DeadlineCreateForm


class DeadlineCreateView(CreateView):
    model = Deadline
    form_class = DeadlineCreateForm
    template_name = 'deadline/create_task.html'
    success_url = '/'
