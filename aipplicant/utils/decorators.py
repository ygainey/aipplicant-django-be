from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from application.models import Application

def handle_exceptions(handler_function):
    def wrapper(*args, **kwargs):
        try:
            return handler_function(*args, **kwargs)
        except (Application.DoesNotExist, NotFound) as e:
            print(e)
            return Response({'message' : str(e)}, 404)
        except PermissionDenied as e:
            print(e)
            return Response ({'message': str(e)}, 403)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
            return Response('Unknown error', 500)
    return wrapper