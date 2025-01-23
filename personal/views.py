from django.shortcuts import render
def home(request):
	context= {}
	return render(request, "personal/home.html")
def privacy_policy(request):
	return render(request, "personal/privacypolicy.html")
