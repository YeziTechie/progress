from django import forms

from tasks.models.time_task import TimeTask


class TimeTaskCreateForm(forms.ModelForm):
    class Meta:
        model = TimeTask
        fields = ['outcome', 'description', 'xp']


class TimeTaskUpdateForm(forms.Form):
    time = forms.CharField(label='time', max_length=5)
