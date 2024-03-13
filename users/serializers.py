from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializer for user data (excluding password)"""
    class Meta:
        model = User
        fields = ('email', 'is_active')  # Add or remove fields as needed

class CreateUserSerializer(serializers.ModelSerializer):
    """Serializer for user creation and token generation"""
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}, 'password2': {'write_only': True}}

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError('Las contraseñas no coinciden')

        return data

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        
        user = User.objects.create_user(email=email, password=password)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': UserSerializer(instance).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }
