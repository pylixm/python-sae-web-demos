# -*-coding:utf-8 -*-
# ===================================
# Created by wuxm on 2015/8/3.
# ===================================
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'toolsBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'blogs.views.home', name='home'),
    url(r'^test/$', 'blogs.views.test'),


)