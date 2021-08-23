from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
"""
class WebsiteCrawlCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteCrawlRequest
        fields = [
            'title',
            'description',
            'url'
        ]

        def validate_title(self, value):
            if len(value) > 100:
                return serializers.ValidationError("Max title length is 100 characters")
            return value

        def validate_description(self, value):
            if len(value) > 200:
                return serializers.ValidationError(
                    "Max description length is 200 characters"
                )
            return value

        def clean_image(self, value):
            initial_path = value.path
            new_path = settings.MEDIA_ROOT + value.name
            os.rename(initial_path, new_path)
            return value
"""