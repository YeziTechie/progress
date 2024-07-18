from django.views.generic.edit import CreateView

from tasks.models.time import Time
from tasks.forms.time import TimeCreateForm


class TimeCreateView(CreateView):
    model = Time
    form_class = TimeCreateForm
    template_name = 'time/create_task.html'
    success_url = '/'
