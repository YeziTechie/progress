from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import FormView

from tasks.models.time import Time
from tasks.forms.time import TimeUpdateForm


class TimeUpdateView(LoginRequiredMixin, FormView):
    form_class = TimeUpdateForm
    template_name = 'time/update.html'
    login_url = 'login'

    def form_valid(self, form):
        task = get_object_or_404(Time, pk=self.kwargs['pk'], owner=self.request.user)
        time = int(form.cleaned_data['time'])
        if time > 0:
            task.total_time += time
            if time > task.longest_time:
                task.longest_time = time
            task.save()
        return redirect(reverse('outcome_detail', kwargs={'pk': task.outcome.pk}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Time, pk=self.kwargs['pk'], owner=self.request.user)
        return context
