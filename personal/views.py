from django.shortcuts import render
def home(request):
	context= {}
	return render(request, "personal/home.html")
# Create your views here.
