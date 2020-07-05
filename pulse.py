#shoutout to lightweight django: https://www.oreilly.com/library/view/lightweight-django/9781491946275/ch01.html
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

import hashlib
import os
import sys
import datetime
import csv

from io import BytesIO
#from PIL import Image, ImageDraw

from django.conf import settings
from django.shortcuts import render#, render_to_response
from django.contrib import admin
#from django.template.loader import get_template from django.apps import AppConfig
from django.apps import AppConfig
from django import template
from django.template.loader import get_template, select_template
from django.core.cache import cache
#from django.core.urlresolvers import reverse
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.views.decorators.http import etag
from django.views.defaults import page_not_found
from django.views.generic.base import TemplateView
from django.template import TemplateDoesNotExist

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

#SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key' }})
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'deamaun.herokuapp.com').split(',')

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#BASE_DIR = os.path.dirname(__file__)
MAIN_DIR = os.path.dirname(os.path.dirname(__file__))
TEMP_PATH = os.path.realpath('.')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#DIRECTOR = r'^app/templates/pulse/templates/pulse'
 
tsela = os.path.join(BASE_DIR, "templates")

TIME_ZONE = 'UTC'

TEMPLATES = [
  {
   'BACKEND':'django.template.backends.django.DjangoTemplates',
   'DIRS':[r'^app/templates/pulse/templates/pulse'],
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
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessagesMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',     
    ),
   INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        #'django.contrib.AccountsConfig',
        'pulse',    
   ),
   STATICFILES_DIRS=(
        os.path.join(BASE_DIR, 'static'),
   ),
   STATIC_URL='/static/',
)

from django.conf.urls import url
#from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.template import loader, Context

PROJECT_DIR = os.path.dirname(__file__)
path = '.'

class LandingView(TemplateView):
  template_name = "pulse.htm"
  
def index(request):
    files = os.listdir(path)

    #for name in files:
    #    #print(os.path.abspath)#(os.path.join(dir,name)),sep='\n')
    #    print('face it: '+os.path.abspath((name)))
         
    for pathMain, dirs, files in os.walk(path):
        print(pathMain)
        for f in files:
            print(f)
    return HttpResponse('Hello World<p><a href="zero" target="_blank">0</a>|<a href="clear" target="_blank">clear</a>|<a href="indecs" target="_blank">indecs</a><br><a href="indecs0" target="_blank">indecs0</a>|<a href="indecs1" target="_blank">indecs1</a><br><a href="indecs2" target="_blank">indecs2</a>|<a href="indecs3" target="_blank">indecs3</a>|<a href="indecs4" target="_blank">indecs4</a>|<a href="one" target="_blank">1</a>|<a href="two" target="_blank">2</a>|<a href="three" target="_blank">3</a><br><a href="four" target="_blank">4</a>|<a href="five" target="_blank">5</a>|<a href="six" target="_blank">6</a>|<a href="seven" target="_blank">7</a>\nalso, HERE IS THE PATH: <u>'+str(tsela)+'</u><br>also '+root("templates")) 

def indecs(request):
    files = os.listdir(BASE_DIR)

    #for name in files:
    #    #print(os.path.abspath)#(os.path.join(dir,name)),sep='\n')
    #    print('face it: '+os.path.abspath((name)))
         
    for pathMain, dirs, files in os.walk(BASE_DIR):
        print(pathMain)
        #for f in files:
        #    print(f)   
    return render(request, 'pulse.html', {"today" : MAIN_DIR})

def indecs0(request):
    files = os.listdir(SETTINGS_PATH)

    #for name in files:
    #    #print(os.path.abspath)#(os.path.join(dir,name)),sep='\n')
    #    print('face it: '+os.path.abspath((name)))
         
    for pathMain, dirs, files in os.walk(SETTINGS_PATH):
        print(pathMain)
        #for f in files:
        #    print(f)
    return render(request, 'pulse.html', {"today" : MAIN_DIR})

def indecs1(request):
    files = os.listdir(MAIN_DIR)

    #for name in files:
    #    #print(os.path.abspath)#(os.path.join(dir,name)),sep='\n')
    #    print('face it: '+os.path.abspath((name)))
         
    for pathMain, dirs, files in os.walk(MAIN_DIR):
        print(pathMain)
        #for f in files:
        #    print(f)
    return render(request, 'pulse.html', {"today" : MAIN_DIR})

def indecs2(request):
    files = os.listdir(TEMP_PATH)

    #for name in files:
    #    #print(os.path.abspath)#(os.path.join(dir,name)),sep='\n')
    #    print('face it: '+os.path.abspath((name)))
         
    for pathMain, dirs, files in os.walk(TEMP_PATH):
        print(pathMain)
        #for f in files:
        #    print(f)      
      
    #return HttpResponse(print("\n\n\n\n\n\nHERE'S THE PATH: "+str(tsela)))  
    #return HttpResponse(render_to_string(render(request, 'pulse.htm', {"today" : name})))
    
    #print('#####################################################################################################################################################################')
    #print('tempPath: '+os.path.join(TEMP_PATH, ' <<'))
    #print('projectDir: '+os.path.join(PROJECT_DIR, ' <<'))
    #print('settingsPath: '+os.path.join(SETTINGS_PATH, ' <<'))
    #print('baseDir: '+os.path.join(BASE_DIR, ' <<'))    
    #print('mainDir: '+os.path.join(MAIN_DIR, ' <<'))
    #print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    return render(request, 'pulse.html', {"today" : MAIN_DIR})
    #return HttpResponse('Hello World<p><a href="zero" target="_blank">0</a>|<a href="one" target="_blank">1</a>|<a href="two" target="_blank">2</a>|<a href="three" target="_blank">3</a>|<a href="four" target="_blank">4</a>|<a href="five" target="_blank">5</a>|<a href="six" target="_blank">6</a>|<a href="seven" target="_blank">7</a>')


def indecs3(request):
    cdr = Cdr.objects.all()
    print('creating csv') 
    file_path = os.path.join(tsela, 'HEREHEREREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEHEREHEREHEREHEREHEHEREHEREHEREHEREHEHERE.csv')
    with open(file_path, 'w') as csvfile:
        file_header =['user', 'clid']
        writer = csv.DictWriter(csvfile, fieldnames=file_header)
        for cd in cdr:
            writer.writerow({'user':'Extend=>'+ str(cd.user), 'clid':cd.clid})    
    
    print('checking mo '+tsela) 
    for pathMain, dirs, files in os.walk(tsela):
        print(pathMain)
        for f in files:
            print(f)
         
    return HttpResponse('e kgonne go kwala csv.')

def indecs4(request):
    cdr = Cdr.objects.all()
    print('creating csv') 
    file_path = 'templates/HEREHEREHEREHEHEREHEREHEREHEREHEHEREHEREHEREHEREHEHEREHEREHEREHEREHEHEREHEREHEREHEREHEHEREHEREHEREHEREHEHEREHEREHEREHEREHEHERE.csv'
    with open(file_path, 'w') as csvfile:
        file_header =['user', 'clid']
        writer = csv.DictWriter(csvfile, fieldnames=file_header)
        for cd in cdr:
            writer.writerow({'user':'Extend=>'+ str(cd.user), 'clid':cd.clid})    
    
    print('checking mo '+tsela) 
    for pathMain, dirs, files in os.walk(tsela):
        print(pathMain)
        for f in files:
            print(f)    
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------')
    
    print('checking mo '+templates) 
    for pathMain, dirs, files in os.walk('templates'):
        print(pathMain)
        for f in files:
            print(f)
         
    return HttpResponse('e kgonne go kwala csv.')
   
def zero(request):
    select_template(['pulse/pulse.html','./pulse.html','pulse.html','templates/pulse.html']) 
    return HttpResponse('This is zero')
#os.path.join(BASE_DIR, 'pulse', 'templates', 'pulse')
#os.path.join(BASE_DIR, 'templates',)

def clear(request):
    print('-----------------------------------------------------------------------------------------------------------------------------------')   
    return render(request, 'pulse.html', {"today" : MAIN_DIR})

def one(request):
       #return HttpResponse(SETTINGS_PATH)
       today = datetime.datetime.now().date()
       #return render(request, 'pulse.htm', {"today" : today})
       #return HttpResponse(os.path.join(SETTINGS_PATH, 'templates'))
       
       #files = os.listdir(path)
       #for name in files:
       #    print(name)
         
       if len(sys.argv) == 2:
           path = sys.argv[1]


       files = os.listdir(path)
       for name in files:
           print(name)

       
       try:
           #select_template("pulse.htm")
           get_template("pulse.htm")
           return render(request, "pulse.htm", {"today" : today})
       except TemplateDoesNotExist:       
           return HttpResponse('this is one.') 
  
'''
def one(request):
   today = datetime.datetime.now().date()
   try:
       get_template("pulse.htm")
       return render(request, "pulse.htm", {"today" : today})
   except TemplateDoesNotExist:
       return HttpResponse(BASE_DIR)
       #raise Http404
'''

def two(request):
    return HttpResponse('two')
 
'''
def three(request):
    return HttpResponse('three')

def four(request):
    return HttpResponse('four')

def five(request):
       today = datetime.datetime.now().date()
       print os.path.join(BASE_DIR, 'templates')
       #return render(request, '/pulse.htm', {"today" : today})
   
def six(request):
       today = datetime.datetime.now().date()
       
       #example = reverse('placeholder', kwargs={'width':50,'height':50})
       #context={
       #   'example':request.build_absolute_uri(example)
       #}
       
       return render(request, 'pulse.htm', {"today" : today})

def seven(request):
       today = datetime.datetime.now().date()
       return render(request, "pulse.htm/", {"today" : today})
'''

urlpatterns = (
    url(r'^$', index, name='homepage'),
    #url(r'^admin/', admin.site.urls),
    url('indecs', indecs, name='indecs'),
    url('indecs0', indecs0, name='indecs0'),
    url('indecs1', indecs1, name='indecs1'),
    url('indecs2', indecs2, name='indecs2'),
    url('indecs3', indecs3, name='indecs3'),
    url('indecs4', indecs4, name='indecs4'),
    url('zero/', zero, name='zero'),
    url('one', one, name='one'),
    url('two', two, name='two'),
    url('clear', clear, name='clear'),
    url(r'^mook/', LandingView.as_view(), name='mook'),
'''
    #url('one', views.one, name="one"),
    url('three', three),
    url('four', four),
    url('five', five),
    url('six', six),
    url('seven', seven),
 '''   
)

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
