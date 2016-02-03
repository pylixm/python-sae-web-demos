#coding:utf-8  
import sae  
  
from toolsblog import wsgi   
  
application = sae.create_wsgi_app(wsgi.application)  
