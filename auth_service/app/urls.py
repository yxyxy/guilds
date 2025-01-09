from django.contrib import admin
from django.urls import path
from auth_service.app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/ldap/', views.ldap_login, name='ldap_login'),
    path('auth/google/', views.google_login, name='google_login'),
    path('auth/apple/', views.apple_login, name='apple_login'),
    path('ab-testing/', views.ab_testing, name='ab_testing'),
]