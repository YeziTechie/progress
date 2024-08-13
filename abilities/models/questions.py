from django.db import models


class OutcomeQuestions(models.Model):
    outcome = models.OneToOneField(
        on_delete=models.CASCADE,
        to='abilities.Outcome',
        null=False,
        related_name='outcome_questions',
    )
    positive = models.TextField(default='Not answered yet.', null=True)
    evidence = models.TextField(default='Not answered yet.', null=True)
    specific = models.TextField(default='Not answered yet.', null=True)
    resource = models.TextField(default='Not answered yet.', null=True)
    control = models.TextField(default='Not answered yet.', null=True)
    identity = models.TextField(default='Not answered yet.', null=True)
    relation_with_other_outcomes = models.TextField(default='Not answered yet.', null=True)
    action = models.TextField(default='Not answered yet.', null=True)
