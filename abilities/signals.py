from django.db.models.signals import post_save
from django.dispatch import receiver

from .models.outcome import Outcome
from .models.questions import OutcomeQuestions
from .models.ecology import ExternalEcology, InternalEcology


@receiver(post_save, sender=Outcome)
def create_related_models(sender, instance, created, **kwargs):
    if created:
        OutcomeQuestions.objects.create(outcome=instance)
        InternalEcology.objects.create(outcome=instance)
        ExternalEcology.objects.create(outcome=instance)
    else:
        if not hasattr(instance, 'related_model_1'):
            OutcomeQuestions.objects.create(outcome=instance)
        if not hasattr(instance, 'related_model_2'):
            InternalEcology.objects.create(outcome=instance)
        if not hasattr(instance, 'related_model_3'):
            ExternalEcology.objects.create(outcome=instance)
