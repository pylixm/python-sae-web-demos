# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iwebtools.views.home', name='home'),
    # url(r'^iwebtools/', include('iwebtools.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$','mytools.views.index'),
    url(r'^markdown/$','mytools.views.markdown'),

)

## django 自动处理静态文件， 在模板框中可直接通过 static/ 引用
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

## u静态文件
#urlpatterns += patterns('',
#     # 匹配static 文件夹及子文件夹中的文件 show_indexes参数，参数设置为True之后，表明可以通过浏览器，包括浏览文件夹及其文件
#     (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': iwebtools.settings.STATICFILES_DIRS,'show_indexes': True}),
#     # 匹配image中的文件
#     #(r'^images/(.*)$' , 'django.views.static.serve', {'document_root': os.path.join( settings.STATIC_PATH , 'images' ) } ) ,
#     # 配置css文件价中的文件及子文件夹中的文件
#     #(r'^css/(?P<path>.*)$' , 'django.views.static.serve', {'document_root': os.path.join( settings.STATIC_PATH , 'css' ) } ) ,
#     #(r'^js/(?P<path>.*)$' , 'django.views.static.serve', {'document_root': os.path.join( settings.STATIC_PATH , 'js' ) } ) ,
#                            )