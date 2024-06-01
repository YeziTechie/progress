from django.urls import path
from .views.list_abilities import AbilityListGenericView
from .views.create_ability import AbilityCreateView
from .views.delete_ability import AbilityDeleteView
from .views.detail_ability import AbilityDetailView

urlpatterns = [
    path('', AbilityListGenericView.as_view(), name='ability_list'),
    path('list/', AbilityListGenericView.as_view(), name='ability_list'),
    path('create/', AbilityCreateView.as_view(), name='ability_create'),
    path('delete/<int:pk>/', AbilityDeleteView.as_view(), name='ability_delete'),
    path('detail/<int:pk>/', AbilityDetailView.as_view(), name='ability_detail'),
]
