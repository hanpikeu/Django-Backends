import os
import subprocess

import psutil
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chinagate.settings')

application = get_wsgi_application()

if len(psutil.Process().children()) == 0:
    subprocess.Popen('python3 discord_bot.py', shell=True)
