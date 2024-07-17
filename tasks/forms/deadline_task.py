from django import forms
from tasks.models.deadline_task import DeadlineTask


class DeadlineTaskCreateForm(forms.ModelForm):
    class Meta:
        model = DeadlineTask
        fields = ['description', 'xp', 'penalty', 'deadline_date', 'duration_days', 'duration_hours']
        widgets = {
            'deadline_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        deadline_date = cleaned_data.get('deadline_date')
        duration_days = cleaned_data.get('duration_days')
        duration_hours = cleaned_data.get('duration_hours')

        if not deadline_date and (duration_days is None and duration_hours is None):
            raise forms.ValidationError("You must specify either a deadline date or a duration.")

        if deadline_date and (duration_days is not None or duration_hours is not None):
            raise forms.ValidationError("You can only specify a deadline date or a duration, not both.")

        return cleaned_data
