from django import forms

from tasks.models.count import Count


class CountCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['description'].widget.attrs['class'] = 'desc-input'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe Your Task..'
        self.fields['description'].widget.attrs['cols'] = '0'
        self.fields['description'].widget.attrs['rows'] = '0'

        self.fields['xp'].widget.attrs['class'] = 'xp-input-elem'

        self.fields['outcome'].required = False

    class Meta:
        model = Count
        fields = ['outcome', 'description', 'xp']


class CountUpdateForm(forms.Form):
    count = forms.CharField(label='count', max_length=5)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['count'].widget.attrs['class'] = 'xp-input-elem'

