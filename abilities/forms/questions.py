from django import forms

from abilities.models.ecology import InternalEcology,  ExternalEcology
from abilities.models.questions import OutcomeQuestions


class ExternalEcologyUpdateForm(forms.ModelForm):
    class Meta:
        model = ExternalEcology
        fields = '__all__'
        exclude = ('outcome',)
        widgets = {
            'q1': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'q2': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'q3': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'q4': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
        }


class InternalEcologyUpdateForm(forms.ModelForm):
    class Meta:
        model = InternalEcology
        fields = '__all__'
        exclude = ('outcome',)
        widgets = {
            'q1': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'q2': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'q3': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'q4': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'q5': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'q6': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'q7': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'q8': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
        }


class OutcomeQuestionsUpdateForm(forms.ModelForm):
    class Meta:
        model = OutcomeQuestions
        fields = '__all__'
        exclude = ('outcome',)
        widgets = {
            'positive': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'evidence': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'specific': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'resource': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'control': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'identity': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'relation_with_other_outcomes': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
            'action': forms.Textarea(attrs={'class': 'desc-input', 'rows': '4'}),
        }
