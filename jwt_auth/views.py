from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .serializers.common import UserSerializer
from aipplicant.utils.decorators import handle_exceptions
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class SignUpView(APIView):
    @handle_exceptions
    def post(self, request):
        user_to_create = UserSerializer(data=request.data)
        if user_to_create.is_valid():
            user = user_to_create.save()
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)
            return Response({
                'message': 'Sign up success',
                'access': access,
                'refresh': str(refresh)
            })

        return Response(user_to_create.errors, status=400)