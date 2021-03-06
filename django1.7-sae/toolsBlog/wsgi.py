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
root = os.path.dirname(__file__)                                             #输出当前文件所在文件夹的绝对路径  
sys.path.insert(0, os.path.join(root, '..', 'site-packages'))                #将root路径中的上级目录的site-packages加入到Path中去  
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "toolsblog.settings")  
  
  
from django.core.wsgi import get_wsgi_application  
application = get_wsgi_application()  