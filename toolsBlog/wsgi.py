#-*- coding:utf-8 -*-
#"""
#WSGI config for toolsBlog project.
#
#It exposes the WSGI callable as a module-level variable named ``application``.
#
#For more information on this file, see
#https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
#"""
#
#import os
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "toolsBlog.settings")
#
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()
import os  
import sys  
root = os.path.dirname(__file__)                                             #�����ǰ�ļ������ļ��еľ���·��  
sys.path.insert(0, os.path.join(root, '..', 'site-packages'))                #��root·���е��ϼ�Ŀ¼��site-packages���뵽Path��ȥ  
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "toolsblog.settings")  
  
  
from django.core.wsgi import get_wsgi_application  
application = get_wsgi_application()  