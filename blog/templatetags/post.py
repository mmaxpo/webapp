from blog.models import Post
from django import template

register = template.Library()


@register.simple_tag()
def post_auther():
    return Post.objects.all()
