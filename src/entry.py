from hello import hello
from js import Response

def on_fetch(request):
    return Response.new(hello("World"))