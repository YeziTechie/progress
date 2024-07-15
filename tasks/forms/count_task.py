from django import forms

from tasks.models.count_task import CountTask


class CountTaskCreateForm(forms.ModelForm):
    class Meta:
        model = CountTask
        fields = ['outcome', 'description', 'xp']


class CountTaskUpdateForm(forms.Form):
    count = forms.CharField(label='count', max_length=5)
