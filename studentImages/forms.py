from django import forms
from account.models import Account
from studentImages.models import Image

class UploadImageFormAdmin(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['title','account','date','image']

class UploadImageFormParent(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['title','date','image']