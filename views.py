def index(request):
    return '<h1>Hello!</h1> Its a home page!'

def post_detail(request, id):
    return '<h1>Post {} page</h1>'.format(id)