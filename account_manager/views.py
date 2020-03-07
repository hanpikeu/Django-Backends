from django.shortcuts import render
from django.views.generic import UpdateView, View
from django.views.defaults import bad_request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Account

from functools import wraps
import secrets


def authenticate(request):
    '''
    쿠키와 세션의 token값을 비교후 boolean을 리턴
    '''
    cookie_id = request.COOKIES.get('token')
    session_id = request.session.get('token')

    return cookie_id and session_id and cookie_id == session_id


def login_required(func=None):
    '''
    장고에서 제공하는 login_required 함수를 재정의합니다.
    인증여부를 판단하는 과정에서 authenticate 함수도 별도로 정의합니다.
    '''
    def _wrapped_view(request, *args, **kwargs):
        if authenticate(request):
            return func(request, *args, **kwargs)  # 인증되면 원래 함수 실행
        else:
            return render(request, 'account_manager/login_required.html', context={})  # 인증 안되면 인증요구 페이지로 이동
    
    return _wrapped_view


class MainView(View):
    '''
    메인 홈페이지 view
    '''
    def get(self, request):
        if request.session.get('token'):
            is_auth = True
        else:
            is_auth = False

        context = {'is_auth': is_auth}
        return render(request, 'main/index.html', context)


class LoginView(View):
    '''
    GET query로 token값을 받아 db와 비교 후 인증하는 view
    '''
    def get(self, request):
        success_url = redirect(reverse('account_manager:main'))

        # 쿠키와 세션으로 인증되면 token 인증 무시
        if authenticate(request):
            # return render(request, 'account_manager/autologin.html', context={})
            return success_url

        else:
            EXPIRE_TIME = 600
            token = self.request.GET.get('token')

            try:
                account = Account.objects.get(token=token)
            except Account.DoesNotExist:
                # 잘못된 토큰값이면 403 bad request
                return bad_request(request, Account.DoesNotExist)

            # 세션에 token 저장
            request.session['token'] = token
            request.session.set_expiry(EXPIRE_TIME)

            # 쿠키에 token 저장
            response = success_url
            response.set_cookie('token', token, max_age=EXPIRE_TIME)

            return response


class Test(View):
    '''
    인증이 필요한 view에서 작동되는지 테스트를 위한 view
    브라우저에 'hello'가 뜨면 정상
    '''
    def get(self, request):
        return render(request, 'account_manager/test.html')