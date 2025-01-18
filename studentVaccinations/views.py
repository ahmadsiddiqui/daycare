from django.shortcuts import render, redirect, get_object_or_404
from studentVaccinations.forms import CreateVaccinationFormAdmin
from studentVaccinations.models import Vaccination
from django.contrib.auth.decorators import login_required
from account.models import Account 
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages

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
