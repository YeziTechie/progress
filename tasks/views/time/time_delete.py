from django.views import generic

from tasks.models.time import Time


class TimeDeleteView(generic.DeleteView):
    model = Time
    context_object_name = 'time'
    template_name = 'time/delete_task.html'
    success_url = '/'
