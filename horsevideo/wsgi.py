"""
WSGI config for horsevideo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import sys, os

# Activate your virtual env
activate_env=os.path.expanduser("/home/django/virtualenvs/videos/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))



sys.path.append('/home/django')
sys.path.append('/home/django/videolibrary')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "horsevideo.settings")





from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
