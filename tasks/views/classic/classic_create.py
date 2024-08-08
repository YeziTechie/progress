from django.views.generic.edit import CreateView

from tasks.models.classic import Classic
from tasks.forms.classic import ClassicCreateForm


class ClassicCreateView(CreateView):
    model = Classic
    form_class = ClassicCreateForm
    template_name = 'classic/create.html'
    success_url = ''
