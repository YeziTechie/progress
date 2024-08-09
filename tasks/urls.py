from django.urls import path

from tasks.views.classic.classic_list import ClassicListView
from tasks.views.classic.classic_create import ClassicCreateView
from tasks.views.classic.classic_delete import ClassicDeleteView
from tasks.views.classic.classic_detail import ClassicDetailView
from tasks.views.classic.classic_update import ClassicUpdateView

from tasks.views.count.count_create import CountCreateView
from tasks.views.count.count_update import CountUpdateView
from tasks.views.count.count_delete import CountDeleteView

from tasks.views.time.time_create import TimeCreateView
from tasks.views.time.time_update import TimeUpdateView
from tasks.views.time.time_delete import TimeDeleteView

from tasks.views.deadline.deadline_create import DeadlineCreateView
from tasks.views.deadline.deadline_delete import DeadlineDeleteView
from tasks.views.deadline.deadline_status import DeadlineStatus
from tasks.views.deadline.deadline_update import DeadlineUpdateView
from tasks.views.deadline.deadline_abort import DeadlineAbortView
from tasks.views.deadline.deadline_repeat import DeadlineRepeatView


urlpatterns = [
    path('classic/list/', ClassicListView.as_view(), name='classic_list'),
    path('<int:outcome_pk>/classic/create/', ClassicCreateView.as_view(), name='classic_create'),
    path('classic/<int:pk>/delete/', ClassicDeleteView.as_view(), name='classic_delete'),
    path('classic/<int:pk>/detail/', ClassicDetailView.as_view(), name='classic_detail'),
    path('classic/<int:pk>/update/', ClassicUpdateView.as_view(), name='classic_update'),

    path('<int:outcome_pk>/count/create/', CountCreateView.as_view(), name='count_create'),
    path('count/<int:pk>/update/', CountUpdateView.as_view(), name='count_update'),
    path('count/<int:pk>/delete/', CountDeleteView.as_view(), name='count_delete'),

    path('<int:outcome_pk>/time/create/', TimeCreateView.as_view(), name='time_create'),
    path('time/<int:pk>/update/', TimeUpdateView.as_view(), name='time_update'),
    path('time/<int:pk>/delete/', TimeDeleteView.as_view(), name='time_delete'),

    path('<int:outcome_pk>/deadline/create/', DeadlineCreateView.as_view(), name='deadline_create'),
    path('deadline/<int:pk>/delete/', DeadlineDeleteView.as_view(), name='deadline_delete'),
    path('deadline/<int:pk>/status/', DeadlineStatus.as_view(), name='deadline_status'),
    path('deadline/<int:pk>/update/', DeadlineUpdateView.as_view(), name='deadline_update'),
    path('deadline/<int:pk>/abort/', DeadlineAbortView.as_view(), name='deadline_abort'),
    path('deadline/<int:pk>/repeat/', DeadlineRepeatView.as_view(), name='deadline_repeat'),

]
