from django.views import generic
from tasks.models.deadline import Deadline


class DeadlineDeleteView(generic.DeleteView):
    model = Deadline
    context_object_name = 'deadline'
    template_name = 'deadline/delete_task.html'
    success_url = '/'
