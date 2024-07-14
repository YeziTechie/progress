from django.urls import path

from tasks.views.classic_task.classic_task_list import ClassicTaskListView
from tasks.views.classic_task.classic_task_create import ClassicTaskCreateView
from tasks.views.classic_task.classic_task_delete import ClassicTaskDeleteView
from tasks.views.classic_task.classic_task_detail import ClassicTaskDetailView
from tasks.views.classic_task.classic_task_update import ClassicTaskUpdateView

from tasks.views.count_task.create_xp_per_count_task import XpPerCountTaskCreateView

urlpatterns = [
    path('classic/list/', ClassicTaskListView.as_view(), name='classic_task_list'),
    path('classic/create/', ClassicTaskCreateView.as_view(), name='classic_task_create'),
    path('classic/delete/<int:pk>/', ClassicTaskDeleteView.as_view(), name='classic_task_delete'),
    path('classic/detail/<int:pk>/', ClassicTaskDetailView.as_view(), name='classic_task_detail'),
    path('classic/update/<int:pk>/', ClassicTaskUpdateView.as_view(), name='classic_task_update'),

    path('xp-per-count/create', XpPerCountTaskCreateView.as_view(), name='xp_per_count_task_create'),
]
