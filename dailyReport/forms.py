from django import forms
from .models import DailyReport

class CreateDailyReportAdmin(forms.ModelForm):
    class Meta:
        model = DailyReport
        fields = '__all__'
        widgets = {
            'account': forms.Select(attrs={'class': ' form-control'}),
            'date': forms.DateInput(attrs={'class': ' form-control', 'type': 'date'}),
            'breakfast': forms.Select(attrs={'class': ' form-control'}),
            'lunch': forms.Select(attrs={'class': ' form-control'}),
            
            'am_nap_start_time': forms.TimeInput(attrs={'class': ' form-control', 'type': 'time'}),
            'am_nap_end_time': forms.TimeInput(attrs={'class': ' form-control', 'type': 'time'}),
            'pm_nap_start_time': forms.TimeInput(attrs={'class': ' form-control', 'type': 'time'}),
            'pm_nap_end_time': forms.TimeInput(attrs={'class': ' form-control', 'type': 'time'}),
            'first_milk_oz': forms.NumberInput(attrs={'class': ' form-control'}),
            'second_milk_oz': forms.NumberInput(attrs={'class': ' form-control'}),
            'third_milk_oz': forms.NumberInput(attrs={'class': ' form-control'}),
            'fourth_milk_oz': forms.NumberInput(attrs={'class': ' form-control'}),
            'first_milk_time': forms.TimeInput(attrs={'class': ' form-control', 'type': 'time'}),
            'second_milk_time': forms.TimeInput(attrs={'class': ' form-control', 'type': 'time'}),
            'third_milk_time': forms.TimeInput(attrs={'class': ' form-control', 'type': 'time'}),
            'fourth_milk_time': forms.TimeInput(attrs={'class': ' form-control', 'type': 'time'}),
           
            'comments': forms.Textarea(attrs={'class': ' form-control'}),
        }
