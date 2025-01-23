from django.shortcuts import render, redirect, get_object_or_404
from studentVaccinations.forms import CreateVaccinationFormAdmin, RecordVaccinationFormAdmin, GetVaccinationRecordAdmin
from studentVaccinations.models import Vaccination, VaccinationRecord, MissingVaccination
from django.contrib.auth.decorators import login_required
from account.models import Account 
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
import calendar
from datetime import datetime

# Create your views here.
def vaccinations_start(request):
	return render(request,"vaccinations_start.html")
@login_required(login_url=reverse_lazy("login"))
def create_vaccination(request):
	if not request.user.is_authenticated:
		return redirect("login")
	if request.user.is_admin:
		form = CreateVaccinationFormAdmin(request.POST or None)
		context = {}
		context['vaccineList'] = Vaccination.objects.all().order_by('requiredAgeInMonths').values()
		if request.method == 'POST':
			form = CreateVaccinationFormAdmin(request.POST)
			if form.is_valid():
				form.save()
				
				return redirect("create_vaccination")
			else:
				form = CreateVaccinationFormAdmin()
				
		context['form'] = form
	else: 
		return HttpResponse("Prohibited")

	return render(request, "create_vaccination.html", context)

def delete_vaccination(request,id):
	obj = get_object_or_404(Vaccination,pk=id)
	if request.user.is_admin:
		obj.delete()
		return redirect("create_vaccination")
	else:
		return HttpResponse("Prohibited")


@login_required(login_url=reverse_lazy("login"))
def record_vaccination(request):
	if not request.user.is_authenticated:
		return redirect("login")
	if request.user.is_admin:
		form = RecordVaccinationFormAdmin(request.POST or None)
		context = {}
		if request.method == 'POST':
			form = RecordVaccinationFormAdmin(request.POST)

			if form.is_valid():
				form.save()
				return redirect("record_vaccination")
			else:
				form=RecordVaccinationFormAdmin()

		context['form']=form
		vaccineList = Vaccination.objects.all()
		context['vaccineList'] = vaccineList
		accountList = Account.objects.all().filter(is_admin=False)
		context['accountList'] = accountList
		context['vaccinationRecord'] = VaccinationRecord.objects.all()
	else:
		return HttpResponse("Prohibited")
	return render(request, "record_vaccination.html", context)	

def delete_record(request,id):
	obj = get_object_or_404(VaccinationRecord,pk=id)
	if request.user.is_admin:
		obj.delete()
		return redirect("vaccination_report")
	else:
		return HttpResponse("Prohibited")

def age_in_months(account):
	today = datetime.now()
	dob = account.date_of_birth
	age_in_years = today.year - dob.year
	age_in_months = today.month - dob.month
	if age_in_months < 0:
		age_in_years -= 1
		age_in_months += 12
	age_in_months += (age_in_years * 12)
	return age_in_months
def generate_missing_vaccinations(account):
	vaccinationRecord = VaccinationRecord.objects.filter(account=account)
	requiredVaccinations = list(Vaccination.objects.filter(requiredAgeInMonths__lte = age_in_months(account)))
	administeredVaccines=list()
	for vac in vaccinationRecord:
		administeredVaccines.append(vac.vaccination)

	filtered = [x for x in requiredVaccinations if x not in administeredVaccines]
	filtered.sort(key=lambda x:x.requiredAgeInMonths)
	for vaccination in filtered:
		missingVaccination = MissingVaccination.objects.get_or_create(account=account, vaccination = vaccination)
	return 0

@login_required(login_url=reverse_lazy("login"))
def vaccination_report(request):
	account=request.user
	vaccinationRecord = VaccinationRecord.objects.filter(account=account)
	if not request.user.is_authenticated:
		return redirect("login")
	if request.user.is_admin:
		context = {}
		context['accountList'] = Account.objects.all().filter(is_admin=False)
		form = GetVaccinationRecordAdmin()
		
		if request.method == 'POST':
			form = GetVaccinationRecordAdmin(request.POST)
			if form.is_valid():
				account = form.cleaned_data["account"]
				vaccinationRecord = VaccinationRecord.objects.filter(account=account)
				context['account'] = account
			else:
				form = GetVaccinationRecordAdmin()
	else:
		vaccinationRecord = VaccinationRecord.objects.filter(account=request.user.id)
		context = {}
		account = request.user
		context['account'] = account

	generate_missing_vaccinations(account)

	missingVaccinations = MissingVaccination.objects.filter(account=account)
	context['is_admin'] = account.is_admin
	context['requiredVaccinations'] = missingVaccinations
	context['age_in_months'] = age_in_months(account)
	context['vaccinationRecord'] = vaccinationRecord
	

	return render (request, "vaccination_report.html", context)

@login_required(login_url=reverse_lazy("login"))
def missing_vaccinations(request):
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_admin:
		return HttpResponse("Prohibited")
	else:
		context={}
		accounts = Account.objects.all().filter(is_admin=False)
		for account in accounts:
			generate_missing_vaccinations(account)
		missing_vaccinations = MissingVaccination.objects.all()
		context['requiredVaccinations'] = missing_vaccinations
	return render(request, "missing_vaccinations.html", context)