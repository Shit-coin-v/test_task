from django.db import models


class User(models.Model):
    name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)

class Post(models.Model):
    body = models.TextField(verbose_name='Пост')
    image = models.ImageField(upload_to='post/')
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
