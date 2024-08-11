from django import forms

from tasks.models.time import Time


class TimeCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['description'].widget.attrs['class'] = 'desc-input'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe Your Task..'
        self.fields['description'].widget.attrs['cols'] = '0'
        self.fields['description'].widget.attrs['rows'] = '0'

        self.fields['xp'].widget.attrs['class'] = 'xp-input-elem'

    class Meta:
        model = Time
        fields = ['outcome', 'description', 'xp']


class TimeUpdateForm(forms.Form):
    time = forms.CharField(label='time', max_length=5)
