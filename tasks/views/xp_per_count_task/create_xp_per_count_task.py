from django.views.generic.edit import CreateView

from tasks.models.xp_per_count import XpPerCountTask
from tasks.forms.xp_per_count_task import XpPerCountTaskCreateForm


class XpPerCountTaskCreateView(CreateView):
    model = XpPerCountTask
    form_class = XpPerCountTaskCreateForm
    template_name = 'xp_per_count_task/create_task.html'
    success_url = ''

