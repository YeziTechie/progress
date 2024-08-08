from django import forms

from tasks.models.classic import Classic


class ClassicCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['description'].widget.attrs['class'] = 'desc-input'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe Your Task..'

    class Meta:
        model = Classic
        fields = ['outcome', 'description', 'xp']


class ClassicUpdateForm(forms.ModelForm):
    class Meta:
        model = Classic
        fields = [
            'report'
        ]
