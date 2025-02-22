from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account
import datetime

def year_choices():
    return [(r) for r in range(datetime.date.today().year-10, datetime.date.today().year+1)]

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length = 60, help_text =" Required, Add a valid email address")
	#date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget(years=year_choices()))

	class Meta:
		model = Account
		fields = ("first_name","last_name","email","password1","password2","date_of_birth",)
		widgets = {
			'date_of_birth':forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
		}


class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")

class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = Account 
		fields = ('email',)

	def clean_email(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			try:
				account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
			except Account.DoesNotExist:
				return email
			raise forms.ValidationError('Email "%s" is already in use' % email)

