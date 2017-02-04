import re
import httplib
from urlparse import parse_qs

class App:
    def __init__(self, routes):
        self.routes = routes

    def __call__(self, environ, start_response):
        url = environ.get('PATH_INFO', '')
        request = dict(
            url=url,
            get=parse_qs(environ.get('QUERY_STRING', '')),
            environ=environ,
        )

        matched_route = False
        for route in self.routes:
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

