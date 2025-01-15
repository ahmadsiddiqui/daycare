from django.db import models
from account.models import Account
from django.utils import timezone


class Image(models.Model):
	title		=models.CharField(max_length = 64, null=False, blank=False, default="unnamed")
	account		=models.ForeignKey(Account, on_delete=models.CASCADE)
	image		=models.ImageField(upload_to = "uploads/")
	date		=models.DateTimeField(default=timezone.now)