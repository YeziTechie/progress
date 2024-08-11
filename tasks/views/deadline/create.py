from django.views.generic.edit import CreateView

from tasks.models.deadline import Deadline
from tasks.forms.deadline import DeadlineCreateForm

from abilities.models.outcome import Outcome


class DeadlineCreateView(CreateView):
    model = Deadline
    form_class = DeadlineCreateForm
    template_name = 'deadline/create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.outcome = Outcome.objects.get(pk=self.kwargs['outcome_pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outcome'] = Outcome.objects.get(pk=self.kwargs['outcome_pk'])
        return context
