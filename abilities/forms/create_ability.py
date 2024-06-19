from django import forms

from abilities.models.outcome import Outcome


class CreateAbilityForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = ['name', 'total_xp']