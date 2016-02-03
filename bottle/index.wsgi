#coding:utf-8

#@app.route('/')
#def hello():
#    return "Hello, world! - Bottle"

import oa
from bottle import default_app

app = default_app()

import sae
application = sae.create_wsgi_app(app)