from django.views.generic.edit import CreateView
from django.urls import reverse

from abilities.models.outcome import Outcome

from tasks.models.count import Count
from tasks.forms.count import CountCreateForm


class CountCreateView(CreateView):
    model = Count
    form_class = CountCreateForm
    template_name = 'count/create.html'

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk})

    def form_valid(self, form):
        form.instance.outcome = Outcome.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outcome'] = Outcome.objects.get(pk=self.kwargs['pk'])
        return context
