from django.views.generic import FormView
from django.shortcuts import redirect, get_object_or_404

from tasks.models.time import Time
from tasks.forms.time import TimeUpdateForm


class TimeUpdateView(FormView):
    form_class = TimeUpdateForm
    template_name = 'time/update_task.html'

    def form_valid(self, form):
        time = int(form.cleaned_data['time'])
        if time > 0:
            time = get_object_or_404(Time, pk=self.kwargs['pk'])
            time.total_time += time
            time.save()

        return redirect('outcome_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = get_object_or_404(Time, pk=self.kwargs['pk'])
        return context
