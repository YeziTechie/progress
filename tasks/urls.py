from django.urls import path

from tasks.views.classic.create import ClassicCreateView
from tasks.views.classic.delete import ClassicDeleteView
from tasks.views.classic.update import ClassicUpdateView

from tasks.views.count.create import CountCreateView
from tasks.views.count.update import CountUpdateView
from tasks.views.count.delete import CountDeleteView

from tasks.views.time.create import TimeCreateView
from tasks.views.time.update import TimeUpdateView
from tasks.views.time.delete import TimeDeleteView

from tasks.views.deadline.create import DeadlineCreateView
from tasks.views.deadline.delete import DeadlineDeleteView
from tasks.views.deadline.status import DeadlineStatus
from tasks.views.deadline.update import DeadlineUpdateView
from tasks.views.deadline.abort import DeadlineAbortView
from tasks.views.deadline.repeat import DeadlineRepeatView


urlpatterns = [
    path('<int:outcome_pk>/classic/create/', ClassicCreateView.as_view(), name='classic_create'),
    path('classic/<int:pk>/delete/', ClassicDeleteView.as_view(), name='classic_delete'),
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
