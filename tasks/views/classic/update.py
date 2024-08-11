from django.views.generic import UpdateView
from django.shortcuts import redirect

from tasks.models.classic import Classic
from tasks.forms.classic import ClassicUpdateForm


class ClassicUpdateView(UpdateView):
    model = Classic
    form_class = ClassicUpdateForm
    template_name = 'classic/update.html'

    def form_valid(self, form):
        task = Classic.objects.get(pk=self.kwargs['pk'])
        task.is_done = True
        task.save()
        return redirect('classic_detail', pk=task.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.object
        return context
