from gevent.pywsgi import WSGIServer
from srv.api_server import app

http_server = WSGIServer(('', 8080), app)
print('SERVING ON :8080')
http_server.serve_forever()