from django.views.generic.edit import CreateView

from abilities.models.outcome import Outcome

from tasks.models.count import Count
from tasks.forms.count import CountCreateForm


class CountCreateView(CreateView):
    model = Count
    form_class = CountCreateForm
    template_name = 'count/create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.outcome = Outcome.objects.get(pk=self.kwargs['outcome_pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outcome'] = Outcome.objects.get(pk=self.kwargs['outcome_pk'])
        return context
