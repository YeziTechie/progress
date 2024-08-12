from django.views.generic.edit import CreateView

from tasks.models.time import Time
from tasks.forms.time import TimeCreateForm

from abilities.models.outcome import Outcome


class TimeCreateView(CreateView):
    model = Time
    form_class = TimeCreateForm
    template_name = 'time/create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.outcome = Outcome.objects.get(pk=self.kwargs['outcome_pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outcome'] = Outcome.objects.get(pk=self.kwargs['outcome_pk'])
        return context

