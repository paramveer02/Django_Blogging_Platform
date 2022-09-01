from django.shortcuts import render

from .models import Post

# context = {
#     "posts": Post.objects.all(),
#     "title": "Home",
# }


def home(request):
    return render(
        request,
        "blog/home.html",
        {"posts": Post.objects.all(), "title": "Home"},
    )


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
