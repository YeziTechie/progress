from django.urls import path
from tasks.views.base_task.list_all_normal_tasks import TaskListView
from tasks.views.base_task.create_normal_task import TaskCreateView
from tasks.views.base_task.delete_normal_task import TaskDeleteView
from tasks.views.base_task.normal_task_detail import TaskDetailView
from tasks.views.base_task.update_normal_task import TaskUpdateView

urlpatterns = [
    path('normal-task/list/', TaskListView.as_view(), name='task_list'),
    path('normal-task/create/', TaskCreateView.as_view(), name='task_create'),
    path('normal-task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('normal-task/detail/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('normal-task/update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
]
