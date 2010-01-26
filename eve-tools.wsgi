PROJECT_ROOT = None

import os, sys
from os.path import join, dirname, abspath, exists

if not PROJECT_ROOT or not exists(PROJECT_ROOT):
    PROJECT_ROOT = dirname(abspath(__file__))

sys.path.append(PROJECT_ROOT)
sys.path.append(join(PROJECT_ROOT, 'pyweb'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'pyweb.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()