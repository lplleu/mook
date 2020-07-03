#shoutout to lightweight django
#02 July 2020
#jedenfalls

#activate postgres
#default admin + key

#register admins
#assign admin roles
#self register
#email/cellphone activation, alert
#what about consultants who are not beapa registered?
#controlled access pages
#annotate pdf
#generate pdf letter
#custom letter
#access controlled stats

import os
import sys
import datetime

from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

#SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key' }})
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'deamaun.herokuapp.com').split(',')

INSTALLED_APPS = [
 'django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 'django.contrib.AccountsConfig',

]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessagesMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
  {
   'BACKEND':'django.template.backends.django.DjangoTemplates',
   'DIRS':[],
   'APP_DIRS':True,
   'OPTIONS':{
       'context_processors':[
          'django.template.context_processors.debug',
          'django.template.context_processors.request',
          'django.contrib.auth.context_processors.auth',
          'django.contrib.messages.context_processors.messages',
       ]},
  }
  ]


#DATABASE = {}

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World<p><a href="zero" target="_blank">0</a>|<a href="one">1</a>|<a href="two">2</a>|<a href="three">3</a>|<a href="four">4</a>')

def zero(request):
    return HttpResponse('This is zero')

def one(request):
   today = datetime.datetime.now().date()
   return render(request, "pulse.htm", {"today" : today})
  
def two(request):
    return HttpResponse('two')

def three(request):
    return HttpResponse('three')

def four(request):
    return HttpResponse('four')


urlpatterns = (
    url(r'^$', index),
    url('zero/', zero),
    url('one', one),
    url('two', two),
    url('three', three),
    url('four', four),
)

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
