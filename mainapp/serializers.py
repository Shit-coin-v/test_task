from rest_framework import serializers, exceptions

from mainapp.models import(
    User, Post, Like, Dislike
)


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = (
            'id',
            'name', 'content', 'date', 
        )


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'id',
            'name', 'content', 'date', 
        )
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 
            'content', 'image',
            'time_create', 'name',
        )

class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(read_only=True, many=True)
    likes = LikeSerializer(read_only=True, many=True)
    dislikes = DislikeSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = (
            'id', 
            'name', 'last_name', 'avatar',
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