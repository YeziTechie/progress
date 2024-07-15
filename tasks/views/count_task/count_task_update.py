from django.views.generic import FormView
from django.shortcuts import redirect, get_object_or_404

from tasks.models.count_task import CountTask
from tasks.forms.count_task import CountTaskUpdateForm


class CountTaskUpdateView(FormView):
    form_class = CountTaskUpdateForm
    template_name = 'count_task/update_task.html'

    def form_valid(self, form):
        count = int(form.cleaned_data['count'])
        if count > 0:
            count_task = get_object_or_404(CountTask, pk=self.kwargs['pk'])
            count_task.total_count += count
            count_task.save()
            print(f"Updated total_count: {count_task.total_count}")

        return redirect('outcome_list')

    # def get_context_data(self, **kwargs):


