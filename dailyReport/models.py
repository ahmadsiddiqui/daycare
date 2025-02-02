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
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Account', null=True)
    date = models.DateField(default=timezone.now, verbose_name='Report Date', null=True)
    breakfast = models.IntegerField(choices=MealCompleteness.choices, verbose_name='Breakfast Completeness', null=True)
    lunch = models.IntegerField(choices=MealCompleteness.choices, verbose_name='Lunch Completeness', null=True)
    had_am_nap = models.BooleanField(verbose_name='Had Morning Nap', null=True)
    had_pm_nap = models.BooleanField(verbose_name='Had Afternoon Nap', null=True)
    am_nap_start_time = models.TimeField(verbose_name='Morning Nap Start Time', null=True)
    am_nap_end_time = models.TimeField(verbose_name='Morning Nap End Time', null=True)
    pm_nap_start_time = models.TimeField(verbose_name='Afternoon Nap Start Time', null=True)
    pm_nap_end_time = models.TimeField(verbose_name='Afternoon Nap End Time', null=True)
    first_milk_oz = models.IntegerField(verbose_name='First Milk (oz)', null=True)
    second_milk_oz = models.IntegerField(verbose_name='Second Milk (oz)', null=True)
    third_milk_oz = models.IntegerField(verbose_name='Third Milk (oz)', null=True)
    fourth_milk_oz = models.IntegerField(verbose_name='Fourth Milk (oz)', null=True)
    first_milk_time = models.TimeField(verbose_name='First Milk Time', null=True)
    second_milk_time = models.TimeField(verbose_name='Second Milk Time', null=True)
    third_milk_time = models.TimeField(verbose_name='Third Milk Time', null=True)
    fourth_milk_time = models.TimeField(verbose_name='Fourth Milk Time', null=True)
    bm_9AM = models.BooleanField(verbose_name='Bowel Movement at 9 AM', null=True)
    bm_10AM = models.BooleanField(verbose_name='Bowel Movement at 10 AM', null=True)
    bm_11AM = models.BooleanField(verbose_name='Bowel Movement at 11 AM', null=True)
    bm_12PM = models.BooleanField(verbose_name='Bowel Movement at 12 PM', null=True)
    bm_1PM = models.BooleanField(verbose_name='Bowel Movement at 1 PM', null=True)
    bm_2PM = models.BooleanField(verbose_name='Bowel Movement at 2 PM', null=True)
    bm_3PM = models.BooleanField(verbose_name='Bowel Movement at 3 PM', null=True)
    bm_4PM = models.BooleanField(verbose_name='Bowel Movement at 4 PM', null=True)
    bm_5PM = models.BooleanField(verbose_name='Bowel Movement at 5 PM', null=True)
    bm_accident_9AM = models.BooleanField(verbose_name='Accident at 9 AM', null=True)
    bm_accident_10AM = models.BooleanField(verbose_name='Accident at 10 AM', null=True)
    bm_accident_11AM = models.BooleanField(verbose_name='Accident at 11 AM', null=True)
    bm_accident_12PM = models.BooleanField(verbose_name='Accident at 12 PM', null=True)
    bm_accident_1PM = models.BooleanField(verbose_name='Accident at 1 PM', null=True)
    bm_accident_2PM = models.BooleanField(verbose_name='Accident at 2 PM', null=True)
    bm_accident_3PM = models.BooleanField(verbose_name='Accident at 3 PM', null=True)
    bm_accident_4PM = models.BooleanField(verbose_name='Accident at 4 PM', null=True)
    bm_accident_5PM = models.BooleanField(verbose_name='Accident at 5 PM', null=True)
    comments = models.TextField(max_length=255, verbose_name='Additional Comments', null=True)
