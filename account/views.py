from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import AccountAuthenticationForm, AccountUpdateForm, RegistrationForm
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from django.http import HttpResponse


@csrf_protect
def registration_view(request):
	if not request.user.is_staff:
		return(HttpResponse("Staff login Required!"))
	context= {}
	form = RegistrationForm(request.POST)
	if request.POST:
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('home')
		else:
			context['registration_form'] = form
	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/registration.html', context)


def registration_request_view(request):
	context ={}
	if request.POST:
		name = request.POST['name']
		email = request.POST['email']
		#send_mail("ADD REQUEST", name, email,["ahmad.siddiqui024@gmail.com"], fail_silently=False)
		f = open('request_file.csv', 'a')
		f.write(name)
		f.write(",")
		f.write(email)
		f.write("\n")
		f.close()
	return render(request, 'account/register_request.html')


def logout_view(request):
	logout(request)
	return redirect('home')

@csrf_protect
def login_view(request):
	context={}

	user = request.user

	if user.is_authenticated:
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email=request.POST['email']
			password=request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request,user)
				return redirect("home")
	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form
	return render(request, 'account/login.html', context)

@csrf_protect
def account_view(request):
	if not request.user.is_authenticated:
		return redirect("login")

	context = {}

	if request.POST:
		form=AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
				"email": request.POST['email'],
				
			}
			form.save()
			context['success_message'] = "Your changes were saved"

	else:
		form = AccountUpdateForm(
			initial = {
				"email": request.user.email,
	
			}
		)
	context['account_form'] = form

	
	return render(request, "account/account.html", context)

def must_authenticate_view(request):
	return render(request, 'account/must_authenticate.html',{})
