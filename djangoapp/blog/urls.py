from blog.views import index
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
]
