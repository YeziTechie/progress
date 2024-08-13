from django.urls import path

from abilities.views.outcome.create_outcome import OutcomeCreateView
from abilities.views.outcome.delete_outcome import OutcomeDeleteView
from abilities.views.outcome.outcome_detail import OutcomeDetailView

from abilities.views.questions.update_external_ecology import ExternalEcologyUpdateView
from abilities.views.questions.update_internal_ecology import InternalEcologyUpdateView
from abilities.views.questions.update_outcome_questions import OutcomeQuestionsUpdateView

urlpatterns = [
    path('create/', OutcomeCreateView.as_view(), name='outcome_create'),
    path('<int:pk>/delete/', OutcomeDeleteView.as_view(), name='outcome_delete'),
    path('<int:pk>/detail/', OutcomeDetailView.as_view(), name='outcome_detail'),

    path('<int:pk>/questions/external-ecology/update/', ExternalEcologyUpdateView.as_view(), name='external-ecology-update'),
    path('<int:pk>/questions/internal-ecology/update/', InternalEcologyUpdateView.as_view(), name='internal-ecology-update'),
    path('<int:pk>/questions/outcome/update/', OutcomeQuestionsUpdateView.as_view(), name='outcome-questions-update'),
]
