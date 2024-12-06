
from django.contrib import admin
from django.urls import path
from agriapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('shop/', views.shop, name='shop'),
    path('sign_farmer/', views.sign_farmer, name='sign_farmer'),
    path('sign_customer/', views.sign_customer, name='sign_customer'),
    path('register_courses/', views.register_courses, name='register_courses'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_courses/', views.admin_courses, name='admin_courses'),
    path('farmers_dashboard/', views.farmers_dashboard, name='farmers_dashboard'),
    path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('shop/', views.shop, name='shop'),
    path('admin_farmers/', views.admin_farmers, name='admin_farmers'),
    path('admin_contact/', views.admin_contacts, name='admin_contact'),
    path('customer/', views.customer, name='customer'),



]
