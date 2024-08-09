from django.views.generic import DeleteView

from tasks.models.classic import Classic


class ClassicDeleteView(DeleteView):
    model = Classic
    context_object_name = 'task'
    template_name = 'classic/delete.html'
    success_url = '/'
