from django import forms

from tasks.models.normal_task import NormalTask


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = NormalTask
        fields = ['outcome', 'description', 'xp']


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = NormalTask
        fields = [
            'report'
        ]
