from django import forms

from tasks.models.time import Time


class TimeCreateForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = ['outcome', 'description', 'xp']


class TimeUpdateForm(forms.Form):
    time = forms.CharField(label='time', max_length=5)
