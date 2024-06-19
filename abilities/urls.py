from django.urls import path
from .views.outcome_list import OutcomeListGenericView
from .views.create_outcome import OutcomeCreateView
from .views.delete_outcome import OutcomeDeleteView
from .views.outcome_detail import OutcomeDetailView

urlpatterns = [
    path('', OutcomeListGenericView.as_view(), name='outcome_list'),
    path('list/', OutcomeListGenericView.as_view(), name='outcome_list'),
    path('create/', OutcomeCreateView.as_view(), name='outcome_create'),
    path('delete/<int:pk>/', OutcomeDeleteView.as_view(), name='outcome_delete'),
    path('detail/<int:pk>/', OutcomeDetailView.as_view(), name='outcome_detail'),
]
