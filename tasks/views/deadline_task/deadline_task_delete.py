from django.views import generic
from tasks.models.deadline_task import DeadlineTask


class DeadlineTaskDeleteView(generic.DeleteView):
    model = DeadlineTask
    context_object_name = 'deadline_task'
    template_name = 'deadline_task/delete_task.html'
    success_url = '/'
