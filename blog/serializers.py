from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Auther, Post, Comment, PostImages


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class AutherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auther
        fields = ['id', 'name', 'email']


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = ['image', 'date_posted', 'post']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'body', 'date_posted']


class PostSerializer(serializers.ModelSerializer):
    author = AutherSerializer()
    images = PostImageSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'body', 'date_posted', 'author', 'images', 'comments']
