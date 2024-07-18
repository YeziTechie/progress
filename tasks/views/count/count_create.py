from django.views.generic.edit import CreateView

from tasks.models.count import Count
from tasks.forms.count import CountCreateForm


class CountCreateView(CreateView):
    model = Count
    form_class = CountCreateForm
    template_name = 'count/create_task.html'
    success_url = '/'
