from django.shortcuts import render, redirect
from studentImages.forms import UploadImageFormAdmin, UploadImageFormParent
from studentImages.models import Image
from account.models import Account
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


# Create your views here.
def show_images_view(request):
	if not request.user.is_authenticated:
		return redirect("login")
	
	context = {}
	
	if request.user.is_admin:
		images = Image.objects.all()
		context['admin']= True
		
	else:
		images = request.user.image_set.all()
		context['admin']= False

	context['images'] = images

	return render(request, 'showImages.html', context)

	

def image_upload(request):
	if not request.user.is_authenticated:
		return redirect("login")
	
	if request.user.is_admin:
		context={}
		form = UploadImageFormAdmin(request.POST or None, request.FILES or None)

		if request.method == 'POST':
			form=UploadImageFormAdmin(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect("success")
			else:
				form = UploadImageFormAdmin()
		context['form'] = form
	else:
		context = {}
		form = UploadImageFormParent(request.POST or None, request.FILES or None)

		if request.method == 'POST':
			form=UploadImageFormParent(request.POST, request.FILES)
			if form.is_valid():
				obj = form.save(commit = False)
				obj.account =request.user.account
				obj.save()
				return redirect("success")
			else:
				form = UploadImageFormParent()
		context['form'] = form

	return render(request, "uploadImage.html", context)
def delete_image_view(request,id):
	obj = get_object_or_404(Image, pk=id)
	if (request.user==obj.account or request.user.is_admin):
		obj.delete()
		return redirect("show_images")

	else:
		return HttpResponse("Prohibited")

	

def success(request):
	return HttpResponse("Image uploaded successfully!")