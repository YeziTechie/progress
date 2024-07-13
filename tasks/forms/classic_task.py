from django import forms

from tasks.models.classic_task import ClassicTask


class ClassicTaskCreateForm(forms.ModelForm):
    class Meta:
        model = ClassicTask
        fields = ['outcome', 'description', 'xp']


class ClassicTaskUpdateForm(forms.ModelForm):
    class Meta:
        model = ClassicTask
        fields = [
            'report'
        ]
