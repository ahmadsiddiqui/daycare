from django.shortcuts import render, redirect, get_object_or_404
from studentVaccinations.forms import CreateVaccinationFormAdmin, RecordVaccinationFormAdmin
from studentVaccinations.models import Vaccination, VaccinationRecord
from django.contrib.auth.decorators import login_required
from account.models import Account 
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
import calendar
import datetime

# Create your views here.
@login_required(login_url=reverse_lazy("login"))
def create_vaccination(request):
	if not request.user.is_authenticated:
		return redirect("login")
	if request.user.is_admin:
		form = CreateVaccinationFormAdmin(request.POST or None)
		context = {}
		context['vaccineList'] = Vaccination.objects.all()
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
		accountList = Account.objects.all()
		context['accountList'] = accountList
		#months=calendar.month_name[1:]
		#context['months']=months
		#days=range(1,32)
		#context['days']=days
		#currentYear = datetime.datetime.now().year
		#years=range(currentYear-10,currentYear+10)
		#context['years']=years
		context['vaccinationRecord'] = VaccinationRecord.objects.all()
	else:
		return HttpResponse("Prohibited")
	return render(request, "record_vaccination.html", context)	

@login_required(login_url=reverse_lazy("login"))
def vaccination_report(request):
	if not request.user.is_authenticated:
		return redirect("login")
	if request.user.is_admin:
		form = GetVaccinationRecordAdmin()
		context = {}
		if request.method == 'POST':
			form = GetVaccinationRecordAdmin(request.POST)
			if form.is_valid():
				account = form.account			
		vaccinationRecord = VaccinationRecord.objects.all().filter(account=account)
		context['vaccinationRecord'] = vaccinationRecord
		return render (request, "vaccination_record.html", context)
	else:
		return HttpResponse("Prohibited")