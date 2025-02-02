from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from account.models import Account
from studentImages.models import Image

class ImageInline(admin.TabularInline):
	model = Image

class AccountAdmin(UserAdmin):
	list_display = ('email','date_joined','last_login','is_admin','is_parent','is_staff','date_of_birth',)
	
	#list_editable = ('is_admin','is_parent','is_staff',)
	search_fields = ('email', 'is_admin')
	readonly_fields = ('date_joined', 'last_login')
	add_form = UserCreationForm
	model = Account

	add_fieldsets =(
    (
        None,
        {
            "fields": ("email","password1","password2","is_admin","is_parent","is_staff",'date_of_birth',),
        }, 
    ),
	)
	inlines = [ImageInline,]

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	ordering = ('email',)



# Register your models here.
admin.site.register(Account, AccountAdmin)

admin.site.unregister(Group)