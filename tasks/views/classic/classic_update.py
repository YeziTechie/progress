from django.views.generic import UpdateView
from django.shortcuts import redirect

from tasks.models.classic import Classic
from tasks.forms.classic import ClassicUpdateForm


class ClassicUpdateView(UpdateView):
    model = Classic
    form_class = ClassicUpdateForm
    template_name = 'classic/update_task.html'

    def form_valid(self, form):
        classic = Classic.objects.get(pk=self.kwargs['pk'])
        classic.is_done = True
        classic.save()
        return redirect('classic_detail', pk=classic.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classic'] = self.object
        return context
