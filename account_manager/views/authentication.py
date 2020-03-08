import datetime
import os
import uuid

from django.http import HttpResponseRedirect, HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.defaults import bad_request
from django.views.generic import View

from account_manager.models.account import Account


def verify_token(token: str):
    """
    토큰이 유효한지 판단합니다.
    """
    try:
        account = Account.objects.get(token=token)
    except Account.DoesNotExist:  # 잘못된 토큰값이면 효력이 없는 토큰
        return False

    if not account.is_able:  # 권한이 없는 유저면 효력이 없는 토큰
        return False

    token_unused_duration = datetime.datetime.now() - account.token_create_time

    if token_unused_duration.seconds > int(os.getenv('COOKIE_EXPIRE_TIME')):  # 방치한 지 일정한 시간이 지났다면 효력이 없는 코드
        return False

    account.token_create_time = datetime.datetime.now()
    account.save()
    return True


def login_required(func=None):
    """
    장고에서 제공하는 login_required 함수를 재정의합니다.
    인증여부를 판단하는 과정에서 authenticate 함수도 별도로 정의합니다.
    """

    def _wrapped_view(request: HttpRequest, *args, **kwargs):
        if verify_token(request.session.get('token')):
            return func(request, *args, **kwargs)  # 인증되면 원래 함수 실행
        else:
            return render(request, 'covidic/login_required.html')  # 인증 안되면 인증요구 페이지로 이동

    return _wrapped_view


def get_cookie(request: HttpRequest):
    """
    토큰을 쿠키에 입력해주는 View 입니다.
    """
    token = request.GET.get('token')

    try:
        account = Account.objects.get(token=token)
    except Account.DoesNotExist:  # 잘못된 토큰값이면 403 bad request
        return bad_request(request, Account.DoesNotExist)

    # 세션에 token 저장
    request.session['token'] = token
    request.session.set_expiry(int(os.getenv('COOKIE_EXPIRE_TIME')))

    return HttpResponseRedirect('/test_auth')


@csrf_exempt
def set_token(request: HttpRequest):
    """
    유저의 토큰를 설정후 반환하는 View입니다.
    [[내부망에서만 호출가능]]
    """
    if request.method != 'GET':  # Wrong Method
        return JsonResponse(status=405)

    if request.headers['Host'] != '127.0.0.1':  # Wrong Host
        return JsonResponse(status=400)

    try:
        account = Account.objects.get(discord_id=request.GET['discord_id'])
    except Account.DoesNotExist:  # Not Exist Account
        return JsonResponse(status=404)

    if not account.is_able:  # Blocked Account
        return JsonResponse(status=402)

    token = uuid.uuid1()
    account.token = token
    account.token_create_time = datetime.datetime.now()
    account.save()

    return JsonResponse({'link': f'http://china-gate.iptime.org/get_cookie?token={token}'})


class TestAuthView(View):
    """
    인증상태를 알려주는 View 입니다.
    """

    def get(self, request: HttpRequest):
        if request.session.get('token'):
            is_auth = True
        else:
            is_auth = False

        context = {'is_auth': is_auth}
        return render(request, 'covidic/test_auth.html', context)
