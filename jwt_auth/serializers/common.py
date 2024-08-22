from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.hashers import make_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_conf = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.pop('password')
        password_conf = data.pop('password_conf')

        if password != password_conf:
            raise serializers.ValidationError({'password_confirmation': 'Passwords do not match.'})
        
        password_validation.validate_password(password=password)

        data['password'] = make_password(password)
        
        return data


    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'professional_summary', 'password', 'password_conf')