from django import forms

from tasks.models.task import Task


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['outcome', 'description', 'xp']