import hmac
import json
import os
import subprocess

from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def webhook(req: HttpRequest):
    if req.method != 'POST':
        return HttpResponse(status=405)

    signature = req.headers['X-Hub-Signature']

    if signature is None:
        return HttpResponse(status=403)

    sha_name, signature = signature.split('=')

    if sha_name != 'sha1':
        return HttpResponse(status=501)

    mac = hmac.new(os.getenv('WEBHOOK_SECRET'), msg=req.body, digestmod='sha1')

    if not hmac.compare_digest(mac.hexdigest(), signature.encode()):
        return HttpResponse(status=403)

    try:
        data = json.loads(req.body.decode('utf-8'))

        if data["ref"] != "refs/heads/master":
            return HttpResponse(status=200)

        if data["repository"]["html_url"] != "https://github.com/China-Gate/Django-Backends":
            return HttpResponse(status=200)

        if data["pusher"]["email"] != "apple01644@gmail.com":
            return HttpResponse(status=200)

        subprocess.Popen('sudo bash update.sh', shell=True)
        return HttpResponse(status=202)
    except Exception:
        return HttpResponse(status=500)
