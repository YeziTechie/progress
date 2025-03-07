from django.views.generic import FormView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from tasks.models.time import Time
from tasks.forms.time import TimeUpdateForm


class TimeUpdateView(FormView):
    form_class = TimeUpdateForm
    template_name = 'time/update.html'

    def form_valid(self, form):
        time = int(form.cleaned_data['time'])
        if time > 0:
            task = get_object_or_404(Time, pk=self.kwargs['pk'])
            task.total_time += time
            if time > task.longest_time:
                task.longest_time = time
            task.save()
            return redirect(reverse('outcome_detail', kwargs={'pk': task.outcome.pk}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Time, pk=self.kwargs['pk'])
        return context
