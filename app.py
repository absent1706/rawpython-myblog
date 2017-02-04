from urlparse import parse_qs

def application(environ, start_response):
    params = parse_qs(environ.get('QUERY_STRING', ''))
    name = params['name'][0] if 'name' in params else 'Bob'

    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['Hello <b>{}</b>'.format(name)]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8081, application)
    srv.serve_forever()