from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .serializers.common import UserSerializer
from aipplicant.utils.decorators import handle_exceptions

User = get_user_model()

# Create your views here.

class SignUpView(APIView):
    @handle_exceptions
    def post(self, request):
        user_to_create = UserSerializer(data=request.data)
        if user_to_create.is_valid():
            user_to_create.save()
            return Response({'message': 'Sign up success'})
        return Response(user_to_create.errors, 400)