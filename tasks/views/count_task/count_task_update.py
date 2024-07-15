from django.views.generic import UpdateView
from django.shortcuts import redirect, get_object_or_404

from tasks.models.count_task import CountTask
from tasks.forms.count_task import CountTaskUpdateForm


class CountTaskUpdateView(UpdateView):
    model = CountTask
    form_class = CountTaskUpdateForm
    template_name = 'count_task/update_task.html'

    def form_valid(self, form):
        count_task = form.save(commit=False)  # Get the instance without saving to the DB yet
        count = int(form.cleaned_data['count'])
        print(f"Form count: {count}")
        print(f"Original total_count: {count_task.total_count}")

        if count > 0:
            count_task.total_count += int(count)  # Update total_count by adding the new count
            count_task.save()
            print(f"Updated total_count: {count_task.total_count}")

        return redirect('outcome_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_task'] = self.object
        return context

