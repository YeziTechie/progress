from django.views.generic import DetailView
from tasks.models.task import Task


# from django.views.generic import FormView
# from django.urls import reverse_lazy
# from django.shortcuts import redirect
# from .forms import TaskDoneForm

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'
