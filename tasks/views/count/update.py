from django.views.generic import FormView
from django.shortcuts import redirect, get_object_or_404

from tasks.models.count import Count
from tasks.forms.count import CountUpdateForm


class CountUpdateView(FormView):
    form_class = CountUpdateForm
    template_name = 'count/update.html'

    def form_valid(self, form):
        count = int(form.cleaned_data['count'])
        if count > 0:
            task = get_object_or_404(Count, pk=self.kwargs['pk'])
            task.total_count += count
            task.save()
        return redirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Count, pk=self.kwargs['pk'])
        return context
