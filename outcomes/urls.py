from django.urls import path

from outcomes.views.outcome.create import OutcomeCreateView
from outcomes.views.outcome.delete import OutcomeDeleteView
from outcomes.views.outcome.detail import OutcomeDetailView

from outcomes.views.outcome.hide_unhide import HideOutcome
from outcomes.views.outcome.set_as_achieved import SetAsAchieved

from outcomes.views.questions.update_external_ecology import ExternalEcologyUpdateView
from outcomes.views.questions.update_internal_ecology import InternalEcologyUpdateView
from outcomes.views.questions.update_outcome_questions import OutcomeQuestionsUpdateView

urlpatterns = [
    path('create/', OutcomeCreateView.as_view(), name='outcome_create'),
    path('<int:pk>/delete/', OutcomeDeleteView.as_view(), name='outcome_delete'),
    path('<int:pk>/detail/', OutcomeDetailView.as_view(), name='outcome_detail'),
    path('<int:pk>/hide/', HideOutcome.as_view(), name='outcome_hide'),
    path('<int:pk>/set-as-achieved/', SetAsAchieved.as_view(), name='outcome_achieve'),

    path('<int:pk>/questions/external-ecology/update/', ExternalEcologyUpdateView.as_view(), name='external_ecology_update'),
    path('<int:pk>/questions/internal-ecology/update/', InternalEcologyUpdateView.as_view(), name='internal_ecology_update'),
    path('<int:pk>/questions/outcome/update/', OutcomeQuestionsUpdateView.as_view(), name='outcome_questions_update'),
]
