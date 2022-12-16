import os
import sys
import platform

#путь к проекту
sys.path.insert(0, '/home/i/industria0/todoapp/public_html')
#путь к фреймворку
sys.path.insert(0, '/home/i/industria0/todoapp/public_html/todoapp')
#путь к виртуальному окружению
sys.path.insert(0, '/home/i/industria0/todoapp/public_html/env/lib/python{0}/site-packages'.format(platform.python_version()[0:3]))
os.environ["DJANGO_SETTINGS_MODULE"] = "todoapp.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()