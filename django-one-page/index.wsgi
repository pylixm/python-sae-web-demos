#def application(environ, start_response):
#    start_response('200 ok', [('content-type', 'text/plain')])
#    return ['Hello, SAE!']

import sae
from iwebtools import wsgi
application = sae.create_wsgi_app(wsgi.application)