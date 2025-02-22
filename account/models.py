from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import pyotp


class MyAccountManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError("Users must have an email address")
	
		user = self.model(
				email=self.normalize_email(email),
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		if not password:
			raise ValueError("Superusers must have a password.")
		user = self.create_user(
				email=self.normalize_email(email),
				password = password,
				)

		user.mfa_hash = pyotp.random_base32()
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user




class Account(AbstractBaseUser):

	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	first_name				= models.CharField(verbose_name ="first name", max_length = 30, default= "")
	last_name				= models.CharField(verbose_name ="last name", max_length = 30, default= "")
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_parent				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	date_of_birth			= models.DateField(null=True, blank= True)
	missing_vaccination		= models.ForeignKey('studentVaccinations.Vaccination', on_delete=models.CASCADE, null=True, blank = True)
	

	USERNAME_FIELD = 'email'

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True
