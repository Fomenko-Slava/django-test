from django.shortcuts import render, get_object_or_404
from django.utils import timezone

#from mysite.utils_helper import prn
from .models import Post

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def fib(num):
    fib_list = [0, 1]
    for i in range(num - 2):
        fib_list.append(fib_list[i] + fib_list[i + 1])

    return fib_list


def post_list(request):
    # html = ', '.join(str(x) for x in fib(8))
    # html = 1/3
    # return HttpResponse(html)

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # prn(posts)
    # print(posts)

    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
