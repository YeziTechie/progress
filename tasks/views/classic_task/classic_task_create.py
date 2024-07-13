from django.views.generic.edit import CreateView
from tasks.models.classic_task import ClassicTask
from tasks.forms.classic_task import ClassicTaskCreateForm


class ClassicTaskCreateView(CreateView):
    model = ClassicTask
    form_class = ClassicTaskCreateForm
    template_name = 'classic_task/create_task.html'
    success_url = ''

