from django.views.generic.edit import CreateView
from django.urls import reverse

from tasks.models.classic import Classic
from tasks.forms.classic import ClassicCreateForm

from abilities.models.outcome import Outcome


class ClassicCreateView(CreateView):
    model = Classic
    form_class = ClassicCreateForm
    template_name = 'classic/create.html'

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk})

    def form_valid(self, form):
        form.instance.outcome = Outcome.objects.get(pk=self.kwargs['outcome_pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outcome'] = Outcome.objects.get(pk=self.kwargs['outcome_pk'])
        return context
