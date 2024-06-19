from django.urls import path
from .views.outcome_list import AbilityListGenericView
from .views.create_outcome import AbilityCreateView
from .views.delete_outcome import AbilityDeleteView
from .views.outcome_detail import AbilityDetailView

urlpatterns = [
    path('', AbilityListGenericView.as_view(), name='ability_list'),
    path('list/', AbilityListGenericView.as_view(), name='ability_list'),
    path('create/', AbilityCreateView.as_view(), name='ability_create'),
    path('delete/<int:pk>/', AbilityDeleteView.as_view(), name='ability_delete'),
    path('detail/<int:pk>/', AbilityDetailView.as_view(), name='ability_detail'),
]
