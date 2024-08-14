from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import redirect

from tasks.models.deadline import Deadline
from tasks.forms.deadline import DeadlineCreateForm

from abilities.models.outcome import Outcome


class DeadlineCreateView(CreateView):
    model = Deadline
    form_class = DeadlineCreateForm
    template_name = 'deadline/create.html'

    def get_success_url(self):
        return redirect(reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk}))

    def form_valid(self, form):
        form.instance.outcome = Outcome.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outcome'] = Outcome.objects.get(pk=self.kwargs['pk'])
        return context
