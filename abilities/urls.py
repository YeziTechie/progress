from django.urls import path
from .views.outcome_list import OutcomeListView
from .views.create_outcome import OutcomeCreateView
from .views.delete_outcome import OutcomeDeleteView
from .views.outcome_detail import OutcomeDetailView

urlpatterns = [
    path('', OutcomeListView.as_view(), name='outcome_list'),
    path('create/', OutcomeCreateView.as_view(), name='outcome_create'),
    path('<int:pk>/delete/', OutcomeDeleteView.as_view(), name='outcome_delete'),
    path('<int:pk>/detail/', OutcomeDetailView.as_view(), name='outcome_detail'),
]
