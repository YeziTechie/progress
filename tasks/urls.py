from django.urls import path

from tasks.views.classic_task.classic_task_list import ClassicTaskListView
from tasks.views.classic_task.classic_task_create import ClassicTaskCreateView
from tasks.views.classic_task.classic_task_delete import ClassicTaskDeleteView
from tasks.views.classic_task.classic_task_detail import ClassicTaskDetailView
from tasks.views.classic_task.classic_task_update import ClassicTaskUpdateView

from tasks.views.count_task.count_task_create import CountTaskCreateView
from tasks.views.count_task.count_task_update import CountTaskUpdateView
from tasks.views.count_task.count_task_delete import CountTaskDeleteView

from tasks.views.time_task.time_task_create import TimeTaskCreateView
from tasks.views.time_task.time_task_update import TimeTaskUpdateView
from tasks.views.time_task.time_task_delete import TimeTaskDeleteView

from tasks.views.deadline_task.deadline_task_create import DeadlineTaskCreateView
from tasks.views.deadline_task.deadline_task_delete import DeadlineTaskDeleteView
from tasks.views.deadline_task.deadline_task_status import DeadlineTaskStatus

urlpatterns = [
    path('classic/list/', ClassicTaskListView.as_view(), name='classic_task_list'),
    path('classic/create/', ClassicTaskCreateView.as_view(), name='classic_task_create'),
    path('classic/<int:pk>/delete/', ClassicTaskDeleteView.as_view(), name='classic_task_delete'),
    path('classic/<int:pk>/detail/', ClassicTaskDetailView.as_view(), name='classic_task_detail'),
    path('classic/<int:pk>/update/', ClassicTaskUpdateView.as_view(), name='classic_task_update'),

    path('count/create/', CountTaskCreateView.as_view(), name='count_task_create'),
    path('count/<int:pk>/update/', CountTaskUpdateView.as_view(), name='count_task_update'),
    path('count/<int:pk>/delete/', CountTaskDeleteView.as_view(), name='count_task_delete'),

    path('time/create/', TimeTaskCreateView.as_view(), name='time_task_create'),
    path('time/<int:pk>/update/', TimeTaskUpdateView.as_view(), name='time_task_update'),
    path('time/<int:pk>/delete/', TimeTaskDeleteView.as_view(), name='time_task_delete'),

    path('deadline/create/', DeadlineTaskCreateView.as_view(), name='deadline_task_create'),
    path('deadline/<int:pk>/delete/', DeadlineTaskDeleteView.as_view(), name='deadline_task_delete'),
    path('deadline/<int:pk>/status/', DeadlineTaskStatus.as_view(), name='deadline_task_status'),

]
