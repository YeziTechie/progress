from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from django.urls import reverse

from tasks.models.count import Count
from tasks.forms.count import CountUpdateForm


class CountUpdateView(LoginRequiredMixin, FormView):
    form_class = CountUpdateForm
    template_name = 'count/update.html'

    def dispatch(self, request, *args, **kwargs):
        # Ensure the user owns the task
        self.task = get_object_or_404(Count, pk=self.kwargs['pk'], outcome__owner=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        count = int(form.cleaned_data['count'])
        if count > 0:
            self.task.total_count += count
            self.task.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.task.outcome.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context
