import mywebpy

from .views import *

app = mywebpy.App([
    dict(regex=r'^/$', view=index),
    dict(regex=r'^/posts/(?P<id>\d+)$', view=post_detail),
])