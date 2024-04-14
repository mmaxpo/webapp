from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from blog.models import Post, Comment, Auther
from blog.serializers import PostSerializer


def post_list(request, pk):
    try:
        post = Post.objects.prefetch_related('comments').get(id=pk)
        comments = post.comments.all()
        post_image = Post.objects.prefetch_related('images').get(id=pk)
        image = post_image.images.all()
    except Post.DoesNotExist:
        return HttpResponse('Post does not exist')
    context = {}
    context['comments'] = comments
    context['image'] = image
    return render(request, 'blog/post_list.html', context=context)


def comment_list(request, pk):
    post = Comment.objects.prefetch_related('post').get(pk=pk)
    return HttpResponse(f"<h1>comment list {post}</h1>")


def like_list(request):
    return HttpResponse("<h1>like list</H1>")


@login_required(login_url='/admin/login/')
@require_http_methods(['GET', 'POST'])
def post_search(request):
    user = request.user
    sesion = request.session.session_key
    title = request.GET.get('q')
    posts = Post.objects.get(title__icontains=title)
    return HttpResponse(f'{posts}')


def post_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    return render(request, 'blog/post_detail.html', {'comment': comment})


class PostDetailsApiView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
