from urlparse import parse_qs

def application(environ, start_response):
    params = parse_qs(environ.get('QUERY_STRING', ''))
    name = params['name'][0] if 'name' in params else 'Bob'

    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['Hello <b>{}</b>'.format(name)]


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 8081, application,
               use_debugger=True,
               use_reloader=True)