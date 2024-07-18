from django.views.generic import DeleteView

from tasks.models.classic import Classic


class ClassicDeleteView(DeleteView):
    model = Classic
    context_object_name = 'classic'
    template_name = 'classic/delete_task.html'
    success_url = ''
