from rest_framework.viewsets import ModelViewSet
from mainapp.models import User, Post, Like
from mainapp.serializers import(
    PostSerializer, UserSerializer, 
    DislikeSerializer, LikeSerializer,
    RegistrationSerializer, 
    AuthenticationSeriallizer,
) 

from django.contrib.auth import get_user_model

Get_user = get_user_model()

from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import(
    HTTP_200_OK, HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN,
)

from rest_framework.views import APIView


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LikeView(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class DislikeView(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = DislikeSerializer

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if Get_user.objects.filter(username=username).exists():
            return Response(
                {'message': 'Пользователь с таким именем сущуствует'},
                status=HTTP_403_FORBIDDEN
            )

        user = Get_user.objects.create_user(
            username=username,
            password=password,
            email=email,
        )

        token = Token.objects.create(user=user)
        return Response({'token': token.key}, HTTP_201_CREATED)

class AuthenticationView(APIView):
    def post(self, request):
        serializer = AuthenticationSeriallizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        username = data.get('username')
        password = data.get('password')

        user = Get_user.objects.filter(username=username).first()

        if user is not None:
            if check_password(password, user.password):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, HTTP_200_OK)
            return Response({'error': 'Пароль не верный'}, HTTP_400_BAD_REQUEST)
        return Response({'error': 'Такого пользователя не существует'}, HTTP_400_BAD_REQUEST)
    
    
    