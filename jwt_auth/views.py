from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .serializers.common import UserSerializer
#from ..utils.decorators import 

User = get_user_model()

# Create your views here.

class SignUpView(APIView):
    
    def post(self, request):
        return Response('Hit Sign Up Routes')