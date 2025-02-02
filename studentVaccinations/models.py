from django.db import models
from account.models import Account


# Create your models here.
class Vaccination(models.Model):
	name					= models.CharField(max_length = 100, unique=True)
	requiredAgeInMonths		= models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.name
	
class VaccinationRecord(models.Model):
	account					= models.ForeignKey(Account, on_delete=models.CASCADE)
	vaccination				= models.ForeignKey(Vaccination, on_delete=models.CASCADE)
	#date_administered		= models.DateField()

class MissingVaccination(models.Model):
	account					= models.ForeignKey(Account, on_delete=models.CASCADE)
	vaccination				= models.ForeignKey(Vaccination, on_delete=models.CASCADE)
