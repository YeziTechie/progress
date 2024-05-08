from django.urls import path
from .views.list_abilities import AbilityListGenericView
from .views.create_ability import AbilityCreateView
from .views.delete_ability import AbilityDeleteView

urlpatterns = [
    path('list/', AbilityListGenericView.as_view(), name='ability_list_generic'),
    path('create/', AbilityCreateView.as_view(), name='ability_create'),
    path('delete/<int:pk>/', AbilityDeleteView.as_view(), name='ability_delete'),
]
