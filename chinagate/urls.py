from django.contrib import admin
from django.urls import path, include
from covidic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.give_otp),
    path('', include('account_manager.urls')),
]
