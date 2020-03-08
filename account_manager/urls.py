from django.urls import path

from account_manager.views.authentication import *

app_name = 'account_manager'

urlpatterns = [
    path('ensure_auth', login_required(TestAuthView.as_view()), name='test_auth'),
    path('test_auth', TestAuthView.as_view(), name='test_auth'),
    path('set_token', set_token, name='set_token'),
    path('get_cookie', get_cookie, name='get_cookie'),
]
