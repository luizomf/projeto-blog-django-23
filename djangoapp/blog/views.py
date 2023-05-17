from django.shortcuts import render


def index(request):
    return render(
        request,
        'blog/pages/index.html'
    )


def page(request):
    return render(
        request,
        'blog/pages/page.html'
    )


def post(request):
    return render(
        request,
        'blog/pages/post.html'
    )
