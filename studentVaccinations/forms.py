from django import forms
from studentVaccinations.models import VaccinationRecord, Vaccination

class CreateVaccinationFormAdmin(forms.ModelForm):
	class Meta:
		model = Vaccination
		fields = ("name", "requiredAgeInMonths")