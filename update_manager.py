import hmac
import json
import os
import re

from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

pattern_migration = re.compile(r'^[^\/]*?\/migrations\/[^\/]*?\.py$')


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

    mac = hmac.new(os.getenv('WEBHOOK_SECRET').encode(), msg=req.body, digestmod='sha1')

    if not hmac.compare_digest(mac.hexdigest().encode(), signature.encode()):
        time.sleep(0.5)
        return HttpResponse(status=403)

    try:
        data = json.loads(req.body.decode('utf-8'))

        if data["ref"] != "refs/heads/master":
            return HttpResponse(status=200)

        if data["repository"]["html_url"] == "https://github.com/China-Gate/Django-Backends":
            if data["pusher"]["email"] != "apple01644@gmail.com":
                return HttpResponse(status=200)

            command = 'sudo bash service_manager/update_repo.sh'
            need_migrate = False
            need_update_discord = False

            for commit in data["commits"]:
                for new_file in commit["added"]:
                    if len(pattern_migration.findall(new_file)) > 0:
                        need_migrate = True
                for change_file in commit["modified"]:
                    if change_file == 'discord_bot.py':
                        need_update_discord = True

            if need_migrate:
                command += ' -m'

            if need_update_discord:
                command += ' -d'

            os.system(command)
            return HttpResponse(status=202)

        return HttpResponse(status=200)
    except Exception:
        return HttpResponse(status=500)
