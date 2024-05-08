from django import forms

from abilities.models.ability import Ability


class CreateAbilityForm(forms.ModelForm):
    class Meta:
        model = Ability
        fields = ['name', 'total_xp']