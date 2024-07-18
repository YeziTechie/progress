from django.views import generic

from tasks.models.count import Count


class CountDeleteView(generic.DeleteView):
    model = Count
    context_object_name = 'count'
    template_name = 'count/delete_task.html'
    success_url = '/'
