from django.shortcuts import render, redirect
def home(request):
	if not request.user.is_authenticated:
		return redirect("login")
	context= {}
	return render(request, "personal/home.html")
def privacy_policy(request):
	return render(request, "personal/privacypolicy.html")
