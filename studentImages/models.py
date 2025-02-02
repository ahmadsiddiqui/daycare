from django.db import models
from account.models import Account
from django.utils import timezone
from django_advance_thumbnail import AdvanceThumbnailField
from django.db.models.signals import post_delete,pre_delete
from django.dispatch import receiver


class Image(models.Model):
	title		=models.CharField(max_length = 64, null=False, blank=False, default="unnamed")
	account		=models.ForeignKey(Account, on_delete=models.CASCADE, null = False)
	image		=models.ImageField(upload_to = "uploads/", null=True, blank=True)
	date		=models.DateTimeField(default=timezone.now)
	thumbnail	=AdvanceThumbnailField(source_field='image', upload_to="thumbnails/", size=(300,300), null=True, blank=True)

@receiver(pre_delete, sender=Image)
def image_delete(sender, instance, *args, **kwargs):
	instance.image.delete()
	instance.thumbnail.delete()
