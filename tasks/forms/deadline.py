from datetime import timedelta
from django.utils import timezone
from django import forms

from tasks.models.deadline import Deadline


class DeadlineCreateForm(forms.ModelForm):
    duration_days = forms.IntegerField(required=False)
    duration_hours = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['description'].widget.attrs['class'] = 'desc-input'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe Your Task..'
        self.fields['description'].widget.attrs['cols'] = '0'
        self.fields['description'].widget.attrs['rows'] = '0'

        self.fields['xp'].widget.attrs['class'] = 'xp-input-elem'
        self.fields['penalty'].widget.attrs['class'] = 'xp-input-elem'

        self.fields['duration_days'].widget.attrs['class'] = 'xp-input-elem'
        self.fields['duration_hours'].widget.attrs['class'] = 'xp-input-elem'
        self.fields['deadline_date'].widget.attrs['class'] = 'xp-input-elem'

    class Meta:
        model = Deadline
        fields = ['description', 'xp', 'penalty', 'deadline_date']
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

        if not deadline_date and (duration_days or duration_hours):
            now = timezone.now()
            days = duration_days or 0
            hours = duration_hours or 0
            cleaned_data['deadline_date'] = now + timedelta(days=days, hours=hours)

        return cleaned_data


class DeadlineUpdateForm(forms.ModelForm):
    class Meta:
        model = Deadline
        fields = ['report']


class DeadlineRepeatForm(forms.ModelForm):
    days = forms.IntegerField(required=False)
    hours = forms.IntegerField(required=False)

    class Meta:
        model = Deadline
        fields = ['deadline_date', 'days', 'hours']
        widgets = {
            'deadline_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        deadline_date = cleaned_data.get('deadline_date')
        days = cleaned_data.get('days')
        hours = cleaned_data.get('hours')

        if not deadline_date and (days is None and hours is None):
            raise forms.ValidationError("You must specify either a deadline date or a duration.")

        if deadline_date and (days is not None or hours is not None):
            raise forms.ValidationError("You can only specify a deadline date or a duration, not both.")

        if not deadline_date and (days or hours):
            now = timezone.now()
            days = days or 0
            hours = hours or 0
            deadline_date = now + timedelta(days=days, hours=hours)

        cleaned_data['deadline_date'] = deadline_date
        return cleaned_data
