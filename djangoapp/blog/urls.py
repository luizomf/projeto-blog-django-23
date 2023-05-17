from blog.views import index, page, post
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('post/', post, name='post'),
    path('page/', page, name='page'),
]
