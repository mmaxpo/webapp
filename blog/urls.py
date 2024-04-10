from django.urls import path

from blog.views import post_list, comment_list, like_list, post_search, post_detail

urlpatterns = [
    path('post/<int:pk>/', post_list),
    path('comment/<int:pk>/', comment_list),
    path('like/', like_list),
    path('search/', post_search),
    path('detail/<int:pk>/', post_detail, name='detail'),

]
