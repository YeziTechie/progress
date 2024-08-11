from django import forms

from tasks.models.classic import Classic


class ClassicCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['description'].widget.attrs['class'] = 'desc-input'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe Your Task..'
        self.fields['description'].widget.attrs['cols'] = '0'
        self.fields['description'].widget.attrs['rows'] = '0'

        self.fields['xp'].widget.attrs['class'] = 'xp-input-elem'

    class Meta:
        model = Classic
        fields = ['description', 'xp', 'outcome']


class ClassicUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['report'].widget.attrs['class'] = 'desc-input'
        self.fields['report'].widget.attrs['placeholder'] = 'How things went on? the result, ' \
                                                            'the process, next step, etc,.'
        self.fields['report'].widget.attrs['cols'] = '0'
        self.fields['report'].widget.attrs['rows'] = '0'

    class Meta:
        model = Classic
        fields = [
            'report'
        ]
