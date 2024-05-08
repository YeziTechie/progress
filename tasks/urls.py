from django.urls import path
from .views.list_all_tasks import TaskListView
from .views.create_task import TaskCreateView
from .views.delete_task import TaskDeleteView
from .views.task_detail import TaskDetailView
from .views.update_task import TaskUpdateView

urlpatterns = [
    path('list/', TaskListView.as_view(), name='task_list_generic'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
]
