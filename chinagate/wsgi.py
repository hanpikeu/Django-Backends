import os
import subprocess

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chinagate.settings')

subprocess.run('python discord_bot.py')
application = get_wsgi_application()
