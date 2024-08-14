from django.db import models


class InternalEcology(models.Model):
    outcome = models.OneToOneField(
        'outcomes.Outcome',
        models.CASCADE,
        related_name='internal_ecology',
        null=False,
    )
    q1 = models.TextField(null=True, blank=False, default='Not answered yet.')
    q2 = models.TextField(null=True, blank=False, default='Not answered yet.')
    q3 = models.TextField(null=True, blank=False, default='Not answered yet.')
    q4 = models.TextField(null=True, blank=False, default='Not answered yet.')
    q5 = models.TextField(null=True, blank=False, default='Not answered yet.')
    q6 = models.TextField(null=True, blank=False, default='Not answered yet.')
    q7 = models.TextField(null=True, blank=False, default='Not answered yet.')
    q8 = models.TextField(null=True, blank=False, default='Not answered yet.')


class ExternalEcology(models.Model):
    outcome = models.OneToOneField(
        'outcomes.Outcome',
        models.CASCADE,
        related_name='external_ecology',
        null=False,
    )

    q1 = models.TextField(null=True, blank=False, default='Not answered yet.')
    q2 = models.TextField(null=True, blank=False, default='Not answered yet.')
    q3 = models.TextField(null=True, blank=False, default='Not answered yet.')
    q4 = models.TextField(null=True, blank=False, default='Not answered yet.')
