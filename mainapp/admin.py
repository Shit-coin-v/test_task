from django.contrib import admin
from mainapp.models import(
    User, Post, Like, Dislike
)

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Dislike)