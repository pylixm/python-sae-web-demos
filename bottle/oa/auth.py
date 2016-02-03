# coding: utf-8
"""
    系统框架结构性功能
"""
from bottle import route ,static_file ,template
from oaconf import app_root


# 首页
@route('/')
def index():
    return template('index.html')

#后台登陆
@route('/admin/login')
def admin_login():
    return template('admin/login.html')

#后台首页
@route('/admin/idx')
def admin_idx():
    return template('admin/main.html')

#后台首页
@route('/admin/content')
def admin_idx():
    return template('admin/content.html')



#后台首页
@route('/test/<name>/<path>')
def index(name,path):
    return template('test.html')

## 静态文件定义
#@route('/resources/:path#.+#')
#def server_static_resources(path):
#    return static_file(path, root = os.path.join(app_root,'resources'))

# 静态文件路径定义
@route('/:path#.+#')
def server_static_resources(path):
    return static_file(path, root = app_root)


