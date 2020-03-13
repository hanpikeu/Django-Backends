from django.contrib import admin
from django.urls import path, include
from update_manager import webhook

urlpatterns = [
    path('webhook/', webhook),
    path('admin/', admin.site.urls),
    path('account_manager/', include('account_manager.urls')),
    path('covidic/', include('covidic.urls')),
    path('notik/', include('notik.urls')),
]
