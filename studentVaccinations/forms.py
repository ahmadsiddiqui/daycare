from django import forms
from account.models import Account
from studentVaccinations.models import VaccinationRecord, Vaccination

class CreateVaccinationFormAdmin(forms.ModelForm):
	class Meta:
		model = Vaccination
		fields = ("name", "requiredAgeInMonths")
class RecordVaccinationFormAdmin(forms.ModelForm):
	class Meta:
		model = VaccinationRecord
		#fields = ("account", "vaccination", "date_administered")
		fields = ("account", "vaccination")

class GetVaccinationRecordAdmin(forms.ModelForm):
	class Meta:
		model = VaccinationRecord
		fields = ("account",)
