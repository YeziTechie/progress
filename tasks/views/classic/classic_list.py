from django.views import generic

from tasks.models.classic import Classic


class ClassicListView(generic.ListView):
    model = Classic
    template_name = 'classic/tasks_list.html'
    context_object_name = 'classic_tasks'
