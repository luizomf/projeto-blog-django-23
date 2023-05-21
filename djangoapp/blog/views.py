from blog.models import Post
from django.core.paginator import Paginator
from django.shortcuts import render

PER_PAGE = 9


def index(request):
    posts = (
        Post
        .objects
        .filter(is_published=True)
        .order_by('-pk')
    )

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def page(request):
    return render(
        request,
        'blog/pages/page.html',
        {
            # 'page_obj': page_obj,
        }
    )


def post(request):
    return render(
        request,
        'blog/pages/post.html',
        {
            # 'page_obj': page_obj,
        }
    )
