from django.shortcuts import render, redirect
from django.http import HttpResponse
from dailyReport.models import DailyReport
from dailyReport.forms import CreateDailyReportAdmin

# Create your views here.

def create_daily_report(request):
	if not request.user.is_authenticated:
		return redirect ("login")
	if not request.user.is_admin:
		return HttpResponse("Prohibited")
	else:
		context = {}
		if request.method == 'POST':
			form = CreateDailyReportAdmin(request.POST)
			if form.is_valid():
				form.save()
			return redirect(create_daily_report)
		else:
			form = CreateDailyReportAdmin()
		context['form'] = form
	return render(request, 'create_daily_report.html',context)
def view_daily_report(request):
	if not request.user.is_authenticated:
		return redirect ("login")