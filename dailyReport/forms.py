from django import forms
from dailyReport.models import DailyReport
class CreateDailyReportAdmin(forms.ModelForm):
	class Meta:
		model = DailyReport
		fields ='__all__'
	