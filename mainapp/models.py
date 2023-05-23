from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    content = models.TextField(verbose_name='Пост')
    image = models.ImageField(upload_to='post/')
    time_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return str(self.user.username)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dislikes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='dislikes')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)
    