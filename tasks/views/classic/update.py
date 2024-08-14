from django.urls import reverse
from django.views.generic import UpdateView
from django.shortcuts import redirect

from tasks.models.classic import Classic
from tasks.forms.classic import ClassicUpdateForm


class ClassicUpdateView(UpdateView):
    model = Classic
    form_class = ClassicUpdateForm
    template_name = 'classic/update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)  # Save the form but don't commit to the database yet
        self.object.is_done = True  # Mark the task as done
        self.object.save()  # Save the object now
        return super().form_valid(form)  # Call the super to handle the redirect

    def get_success_url(self):
        return redirect(reverse('outcome_detail', kwargs={'pk': self.object.outcome.pk}))
