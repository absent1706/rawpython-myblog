def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['Hello <b>Bob</b>!']

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8081, application)
    srv.serve_forever()