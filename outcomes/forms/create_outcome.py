from django import forms

from outcomes.models.outcome import Outcome


class CreateOutcomeForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = ['name', 'total_xp']