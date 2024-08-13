from django import forms

from abilities.models.outcome import Outcome


class OutcomeCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'desc-input'
        self.fields['name'].widget.attrs['placeholder'] = 'e.g. Master Thyself, Learn astral travel, survival skills..'

    class Meta:
        model = Outcome
        fields = ['name']
