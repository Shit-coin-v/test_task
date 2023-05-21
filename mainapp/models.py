from django.db import models


class User(models.Model):
    name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    avatar = models.ImageField(upload_to='user/', blank=True)

    def __str__(self):
        return str(f'{self.name} {self.last_name}')

class Post(models.Model):
    content = models.TextField(verbose_name='Пост')
    image = models.ImageField(upload_to='post/')
    time_create = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return str(self.name)

class Like(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    content = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Dislike(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dislikes')
    content = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

@property
def like_amount(self):
    return self.like.count()

@property
def dislike_amount(self):
    return self.dislike.count()
