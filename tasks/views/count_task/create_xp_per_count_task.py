from django.views.generic.edit import CreateView

from tasks.models.count_task import CountTask
from tasks.forms.count_task import CountTaskCreateForm


class CountTaskCreateView(CreateView):
    model = CountTask
    form_class = CountTaskCreateForm
    template_name = 'count_task/create_task.html'
    success_url = ''

