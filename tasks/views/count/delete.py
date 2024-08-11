from django.views import generic

from tasks.models.count import Count


class CountDeleteView(generic.DeleteView):
    model = Count
    context_object_name = 'task'
    template_name = 'count/delete.html'
    success_url = '/'
