from django.views.generic import FormView
from django.shortcuts import get_object_or_404, redirect

from tasks.models.deadline import Deadline
from tasks.forms.deadline import DeadlineRepeatForm


class DeadlineRepeatView(FormView):
    template_name = 'deadline/repeat.html'
    form_class = DeadlineRepeatForm
    success_url = '/'

    def form_valid(self, form):
        obj = get_object_or_404(Deadline, pk=self.kwargs['pk'])
        if obj.is_time_over():
            date = form.cleaned_data.get('deadline_date')
            print(date)
            obj.deadline_date = date
            obj.save()
            return redirect(self.success_url)
        else:
            raise Exception('The duration of this task is not over yet. You still have time.'.title())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = get_object_or_404(Deadline, pk=self.kwargs['pk'])
        if not obj.is_time_over():
            raise Exception('The duration of this task is not over yet. You still have time.'.title())
        context['obj'] = obj
        return context
