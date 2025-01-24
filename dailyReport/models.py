from django.db import models
from account.models import Account
from django.utils import timezone

# Create your models here
class DailyReport(models.Model):
	class MealCompleteness(models.IntegerChoices):
		DID_NOT_EAT = 0
		ATE_A_LITTLE = 1
		ATE_MOST = 2
		ATE_ALL = 3
	
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	date = models.DateField(default=timezone.now())
	breakfast = models.IntegerField(choices=MealCompleteness)
	lunch = models.IntegerField(choices=MealCompleteness)
	had_am_nap = models.BooleanField()
	had_pm_nap = models.BooleanField()
	am_nap_start_time = models.TimeField()
	am_nap_end_time	= models.TimeField()
	first_milk_oz = models.IntegerField()
	second_milk_oz = models.IntegerField()
	third_milk_oz = models.IntegerField()
	fourth_milk_oz = models.IntegerField()
	first_milk_time = models.TimeField()
	second_milk_time = models.TimeField()
	third_milk_time = models.TimeField()
	fourth_milk_time = models.TimeField()
	bm_9AM = models.BooleanField()
	bm_10AM = models.BooleanField()
	bm_11AM = models.BooleanField()
	bm_12PM = models.BooleanField()
	bm_1PM = models.BooleanField()
	bm_2PM = models.BooleanField()
	bm_3PM = models.BooleanField()
	bm_4PM = models.BooleanField()
	bm_5PM = models.BooleanField()
	bm_9AM = models.BooleanField()
	bm_accident_10AM = models.BooleanField()
	bm_accident_11AM = models.BooleanField()
	bm_accident_12PM = models.BooleanField()
	bm_accident_1PM = models.BooleanField()
	bm_accident_2PM = models.BooleanField()
	bm_accident_3PM = models.BooleanField()
	bm_accident_4PM = models.BooleanField()
	bm_accident_5PM = models.BooleanField()
	comments = models.TextField(max_length=255)
