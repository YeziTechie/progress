from django.urls import path

from tasks.views.classic_task.classic_task_list import ClassicTaskListView
from tasks.views.classic_task.classic_task_create import ClassicTaskCreateView
from tasks.views.classic_task.classic_task_delete import ClassicTaskDeleteView
from tasks.views.classic_task.classic_task_detail import ClassicTaskDetailView
from tasks.views.classic_task.classic_task_update import ClassicTaskUpdateView

from tasks.views.count_task.count_task_create import CountTaskCreateView
from tasks.views.count_task.count_task_update import CountTaskUpdateView

urlpatterns = [
    path('classic/list/', ClassicTaskListView.as_view(), name='classic_task_list'),
    path('classic/create/', ClassicTaskCreateView.as_view(), name='classic_task_create'),
    path('classic/<int:pk>/delete/', ClassicTaskDeleteView.as_view(), name='classic_task_delete'),
    path('classic/<int:pk>/detail/', ClassicTaskDetailView.as_view(), name='classic_task_detail'),
    path('classic/<int:pk>/update/', ClassicTaskUpdateView.as_view(), name='classic_task_update'),

    path('count/create/', CountTaskCreateView.as_view(), name='count_task_create'),
    path('count/<int:pk>/update/', CountTaskUpdateView.as_view(), name='count_task_update'),
]
