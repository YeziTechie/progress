from django.views.generic import FormView
from django.shortcuts import redirect, get_object_or_404

from tasks.models.count import Count
from tasks.forms.count import CountUpdateForm


class CountUpdateView(FormView):
    form_class = CountUpdateForm
    template_name = 'count/update_task.html'

    def form_valid(self, form):
        count = int(form.cleaned_data['count'])
        if count > 0:
            count = get_object_or_404(Count, pk=self.kwargs['pk'])
            count.total_count += count
            count.save()
        return redirect('outcome_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = get_object_or_404(Count, pk=self.kwargs['pk'])
        return context
