from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

class AccountAdmin(UserAdmin):
	list_display = ('email','date_joined','last_login','is_admin','is_parent','is_staff')
	search_fields = ('email',)
	readonly_fields = ('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	ordering = ('email',)
# Register your models here.
admin.site.register(Account, AccountAdmin)