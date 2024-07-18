from django.views.generic import DetailView

from tasks.models.classic import Classic


class ClassicDetailView(DetailView):
    model = Classic
    context_object_name = 'classic'
    template_name = 'classic/task_detail.html'
