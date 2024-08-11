from django.views import generic
from tasks.models.deadline import Deadline


class DeadlineDeleteView(generic.DeleteView):
    model = Deadline
    context_object_name = 'task'
    template_name = 'deadline/delete.html'
    success_url = '/'
