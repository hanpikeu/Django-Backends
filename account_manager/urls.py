from django.urls import path
from . import views
from .views import login_required


app_name = 'account_manager'
urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('autologin/', views.LoginView.as_view(), name='autologin'),
    path('test/login', login_required(views.Test.as_view()), name='test_login'),
]
