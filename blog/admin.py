from django.contrib import admin
from blog.models import *


@admin.register(Auther)
class AutherAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name']


class PostAdminInline(admin.TabularInline):
    model = PostImages
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'date_posted']
    search_fields = ['title', 'user']
    inlines = [PostAdminInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'date_posted']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'date_posted']


@admin.register(PostImages)
class PostImagesAdmin(admin.ModelAdmin):
    list_display = ['image', 'post', 'date_posted']
