import re
import httplib
from urlparse import parse_qs

from views import *

routes = [
    dict(regex=r'^/$', view=index),
    dict(regex=r'^/posts/(?P<id>\d+)$', view=post_detail),
]

def application(environ, start_response):
    url = environ.get('PATH_INFO', '')
    request = dict(
        url=url,
        get=parse_qs(environ.get('QUERY_STRING', '')),
        environ=environ,
    )

    matched_route = False
    for route in routes:
        match = re.match(route['regex'], url)
        if match:
            kwargs = match.groupdict()
            response = route['view'](request, **kwargs)
            # if resp is just a string, assert 200 code and some headers
            # otherwise just take it assuming it's a tuple of suggested format
            code, headers, body = 200, {'Content-Type': 'text/html'}, response\
                                  if isinstance(response, basestring) \
                                  else response
            matched_route = True
            break
    if not matched_route:
        code, headers, body = 404, {'Content-Type': 'text/html'}, \
                              '<h1>Sorry, page does not exist</h1>'

    start_response('{} {}'.format(code, httplib.responses[code]),
                   headers.items())
    return body


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 8081, application,
               use_debugger=True,
               use_reloader=True)