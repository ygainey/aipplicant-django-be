from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers.common import UserProfileSerializer
from jwt_auth.models import User
from aipplicant.utils.decorators import handle_exceptions
# Create your views here.

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @handle_exceptions
    def get(self, request): #tested and working on postman
       user = request.user
       serialized_user = UserProfileSerializer(user)
       return Response(serialized_user.data) 
    
    @handle_exceptions
    def put(self, request): #test and working on postman
        user = request.user
        serialized_user = UserProfileSerializer(user, data=request.data, partial=True)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serialized_user.data)
        return Response(serialized_user.errors, 400)