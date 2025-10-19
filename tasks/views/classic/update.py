from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse

from tasks.models.classic import Classic
from tasks.forms.classic import ClassicUpdateForm


class ClassicUpdateView(LoginRequiredMixin, UpdateView):
    model = Classic
    form_class = ClassicUpdateForm
    template_name = 'classic/update.html'
    context_object_name = 'task'

    def get_object(self, queryset=None):
        # Only allow updates if the user owns the outcome linked to the task
        obj = super().get_object(queryset)
        if obj.outcome.owner != self.request.user:
            raise PermissionError("You do not have permission to edit this task.")
        return obj

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_done = True
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk})
