import mywebpy

from views import *

app = mywebpy.App([
    dict(regex=r'^/$', view=index),
    dict(regex=r'^/posts/(?P<id>\d+)$', view=post_detail),
])

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 8081, app,
               use_debugger=True,
               use_reloader=True)