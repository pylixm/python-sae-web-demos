# coding: utf-8


import oa ,sys ,os
ROOT = os.path.abspath( os.path.split( __file__ )[0] )
sys.path.append( ROOT )

from bottle import run ,debug ,default_app
try:
    from oaconf import app_debug
except:
    app_debug = False

debug(app_debug)   # 是否在调试状态下

app = default_app()

# 启动服务
run(app=app ,host='localhost', port=9000 ,reloader=True)

