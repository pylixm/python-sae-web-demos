#-*- coding:utf-8 -*-
"""
Django settings for toolsBlog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os  
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  
import os.path   

from os import environ  
debug = not environ.get("APP_NAME", "")   
if debug:  
#LOCAL 本地调试用，便于导出数据库,根据本地MYSQL数据库填写下面参数<----------------如果文件中出现中文，一定要在开始添加 #coding:utf-8  
    MYSQL_DB = 'toolsblog'
    MYSQL_USER = 'root'   
    MYSQL_PASS = 'root'
    MYSQL_HOST_M = '127.0.0.1'   
    MYSQL_HOST_S = '127.0.0.1'   
    MYSQL_PORT = '3306'   
else:   
#SAE   
    import sae.const   
    MYSQL_DB = sae.const.MYSQL_DB   
    MYSQL_USER = sae.const.MYSQL_USER   
    MYSQL_PASS = sae.const.MYSQL_PASS   
    MYSQL_HOST_M = sae.const.MYSQL_HOST   
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S   
    MYSQL_PORT = sae.const.MYSQL_PORT  
    
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',   
        'NAME': MYSQL_DB,   
        'USER': MYSQL_USER,   
        'PASSWORD': MYSQL_PASS,   
        'HOST': MYSQL_HOST_M,   
        'PORT': MYSQL_PORT,   
    }  
} 
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lft@!^***imx1i$dp+l_^)8)!vlt_le^p9ho1(f4lyke@ir&zz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogs',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'toolsblog.urls'

WSGI_APPLICATION = 'toolsblog.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = '/static/'

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)