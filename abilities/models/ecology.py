from django.db import models

from outcome import Outcome


class InternalEcology(models.Model):
    outcome = models.OneToOneField(
        on_delete=models.CASCADE,
        to=Outcome,
        null=False
    )
    q1 = models.CharField(max_length=512, null=True, blank=False, default='Not answered yet.')
    q2 = models.CharField(max_length=256, null=True, blank=False, default='Not answered yet.')
    q3 = models.CharField(max_length=256, null=True, blank=False, default='Not answered yet.')
    q4 = models.CharField(max_length=128, null=True, blank=False, default='Not answered yet.')
    q5 = models.CharField(max_length=512, null=True, blank=False, default='Not answered yet.')
    q6 = models.CharField(max_length=512, null=True, blank=False, default='Not answered yet.')
    q7 = models.CharField(max_length=512, null=True, blank=False, default='Not answered yet.')
    q8 = models.CharField(max_length=512, null=True, blank=False, default='Not answered yet.')


class ExternalEcology(models.Model):
    outcome = models.OneToOneField(
        on_delete=models.CASCADE,
        to=Outcome,
        null=False
    )

    q1 = models.CharField(max_length=256, null=True, blank=False, default='Not answered yet.')
    q2 = models.CharField(max_length=256, null=True, blank=False, default='Not answered yet.')
    q3 = models.CharField(max_length=256, null=True, blank=False, default='Not answered yet.')
    q4 = models.CharField(max_length=256, null=True, blank=False, default='Not answered yet.')
