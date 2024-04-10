from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Auther(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(
        max_length=200, unique=True
    )
    body = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Auther, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        reverse


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class PostImages(models.Model):
    image = models.ImageField(upload_to='posts/')
    date_posted = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
