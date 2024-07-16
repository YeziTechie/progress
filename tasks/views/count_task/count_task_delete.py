from django.views import generic
from tasks.models.count_task import CountTask


class CountTaskDeleteView(generic.DeleteView):
    model = CountTask
    context_object_name = 'count_task'
    template_name = 'count_task/delete_task.html'
    success_url = '/'
