from rest_framework import serializers, exceptions

from mainapp.models import(
    User, Post, Like,
)

class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = (
            'id', 'body', 'image',
            'user_name', 'likes',
        )

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'name', 'last_name',
        )

class LikeSerializer(serializers.Serializer):
    class Meta:
        model = Like
        fields = (
            'id',
            'user', 'post', 'date',
        )

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

    def validated_password(self, value):
        if len(value) < 6:
            raise exceptions.ValidationError('Пароль слишком короткий')                  
        elif len(value) > 20:
            raise exceptions.ValidationError('Пароль слишком длинный')
        return value

class AuthenticationSeriallizer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()