from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied

def handle_exceptions(handler_function):
    def wrapper(*args, **kwargs):
        try:
            return handler_function(*args, **kwargs)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
            return Response('Unknown error', 500)
    return wrapper