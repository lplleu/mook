# props to lightweight django for making everything possible
# jedenfalls
# 02 July 2020

import os
import sys

from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

#SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key' }})
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'deamaun.herokuapp.com').split(',')

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
    return HttpResponse('Hello World<p><a href="zero" target_="blank">0</a>|<a href="one">1</a>|<a href=two"">2</a>|<a href="three">3</a>|<a href="four">4</a>')

def zero(request):
    return HttpResponse('This is zero')

def one(request):
    return HttpResponse('one')

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
