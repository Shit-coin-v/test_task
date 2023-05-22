from rest_framework import serializers, exceptions

from django.contrib.auth import get_user_model

User = get_user_model()

from mainapp.models import(
    Post, Like, Dislike
)


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = (
            'id',
            'user', 'post', 'date', 
        )


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'id',
            'user', 'post', 'date', 
        )
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 
            'content', 'image',
            'time_create', 'user',
        )

class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(read_only=True, many=True)
    likes = LikeSerializer(read_only=True, many=True)
    dislikes = DislikeSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = (
            'id', 
            'user_name', 'last_name',
            'posts', 'likes', 'dislikes',
        )
class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

    def validated_password(self, value):
        if len(value) < 6:
            raise exceptions.ValidationError('Пароль слишком короткий')                  
        elif len(value) > 20:
            raise exceptions.ValidationError('Пароль слишком длинный')
        return value

class AuthenticationSeriallizer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()