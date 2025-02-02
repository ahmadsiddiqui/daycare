from django import forms
from account.models import Account
from studentImages.models import Image

class UploadImageFormAdmin(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['title','account','date','image']
		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control'}),
			'account':forms.Select(attrs={'class':'form-control'}),
			'date':forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
			'image':forms.FileInput(attrs={'class':'form-control'}),
		}

class UploadImageFormParent(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['title','date','image']