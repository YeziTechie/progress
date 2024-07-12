from django.views.generic.edit import CreateView

from tasks.models.xp_per_count import XpPerCountTask
from tasks.forms.xp_per_count_task import CreateXpPerCountTaskForm


class XpPerCountTaskCreateView(CreateView):
    model = XpPerCountTask
    form_class = CreateXpPerCountTaskForm
    template_name = 'xp_per_count_task/create_task.html'
    success_url = '/tasks/list/'

