from django import forms

from tasks.models.count import Count


class CountCreateForm(forms.ModelForm):
    class Meta:
        model = Count
        fields = ['outcome', 'description', 'xp']


class CountUpdateForm(forms.Form):
    count = forms.CharField(label='count', max_length=5)
