# Alexandria/primer/views.py

from django.http import HttpResponse

def say_hello(request):
    message = "Hello world!"

    return HttpResponse(message, content_type="text/plain")
