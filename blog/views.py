import time

from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from blog.models import Blog


# Create your views here.


def greeting(request):
    return render(request, "greeting.html")


@cache_page(60 * 15)
def blog_view(request, blog_id: int):
    blog = get_object_or_404(Blog, id=blog_id)
    time.sleep(3)
    return render(request, "blog.html", {"blog": blog})
