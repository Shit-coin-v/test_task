from rest_framework.routers import DefaultRouter as DR
from django.urls import path

from mainapp.views import(
    UserView, PostView, LikeView, DislikeView,
    RegistrationView, AuthenticationView,
)


router = DR()

router.register('user', UserView)
router.register('posts', PostView)
router.register('likes', LikeView)
router.register('dislikes', DislikeView)



urlpatterns = [
    path('reg/', RegistrationView.as_view()),
    path('auth/', AuthenticationView.as_view()),
]

urlpatterns += router.urls