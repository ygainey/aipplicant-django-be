from rest_framework.serializers import ModelSerializer
from jwt_auth.models import User

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'professional_summary')