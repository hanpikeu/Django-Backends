from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account_manager/', include('account_manager.urls')),
    path('covidic/', include('covidic.urls')),
    path('notik/', include('notik.urls')),
]
