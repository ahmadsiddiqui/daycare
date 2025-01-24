from django.contrib import admin
from django.urls import path
from account.views import *
from personal.views import *
from studentImages.views import *
from studentVaccinations.views import *
from dailyReport.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name="home"),
    path('privacy', privacy_policy, name="privacy"),
    path('admin/', admin.site.urls, name="admin"),
    path('account/', account_view, name="account"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('must_authenticate/', must_authenticate_view, name="must_authenticate"),
    path('register_request/', registration_request_view, name="register_request"),
    path('studentImages/upload',image_upload, name="upload"),
    path('success', success, name="success"),
    path('account/registration', registration_view, name="account_registration"),
    path('studentImages/show',show_images_view,name='show_images'),
    path('studentImages/delete/<int:id>',delete_image_view, name='delete_image'),
    path('studentVaccinations/create', create_vaccination, name="create_vaccination"),
    path('studentVaccinations/delete/<int:id>', delete_vaccination, name="delete_vaccination"),
    path('studentVaccinations/record', record_vaccination, name="record_vaccination"),
    path('studentVaccinations/view_report',vaccination_report, name="vaccination_report"),
    path('studentVaccinations/delete_record/<int:id>',delete_record, name="delete_record"),
    path('studentVaccinations/missing_vaccinations',missing_vaccinations, name="missing_vaccinations"),
    path('studentVaccinations/',vaccinations_start, name="vaccinations_start"),
    path('dailyReport/create', create_daily_report, name="create_daily_report"),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

