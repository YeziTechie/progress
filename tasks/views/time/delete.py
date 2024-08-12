from django.views import generic

from tasks.models.time import Time


class TimeDeleteView(generic.DeleteView):
    model = Time
    context_object_name = 'task'
    template_name = 'time/delete.html'
    success_url = '/'
