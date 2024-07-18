from django import forms

from tasks.models.classic import Classic


class ClassicCreateForm(forms.ModelForm):
    class Meta:
        model = Classic
        fields = ['outcome', 'description', 'xp']


class ClassicUpdateForm(forms.ModelForm):
    class Meta:
        model = Classic
        fields = [
            'report'
        ]
