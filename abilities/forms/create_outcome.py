from django import forms

from abilities.models.outcome import Outcome


class OutcomeCreateForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = ['name']
