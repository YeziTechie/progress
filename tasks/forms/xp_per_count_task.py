from django import forms

from tasks.models.xp_per_count import XpPerCountTask


class XpPerCountTaskCreateForm(forms.ModelForm):
    class Meta:
        model = XpPerCountTask
        fields = ['outcome', 'description', 'xp']

