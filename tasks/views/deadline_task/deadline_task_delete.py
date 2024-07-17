from django.views import generic
from tasks.models.time_task import TimeTask


class TimeTaskDeleteView(generic.DeleteView):
    model = TimeTask
    context_object_name = 'time_task'
    template_name = 'time_task/delete_task.html'
    success_url = '/'
