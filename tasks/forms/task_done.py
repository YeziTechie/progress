from django import forms
from tasks.models.task import Task


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'report'
        ]
