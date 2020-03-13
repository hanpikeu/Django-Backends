import json
import subprocess

from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def webhook(req: HttpRequest):
    print(req)
    if req.method != 'POST':
        return HttpResponse(status=405)

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
