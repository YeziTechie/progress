from django import forms
from tasks.models.normal_task import NormalTask


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = NormalTask
        fields = [
            'report'
        ]
