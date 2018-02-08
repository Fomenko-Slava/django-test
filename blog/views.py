from django.shortcuts import render

#from django.http import HttpResponse
# import datetime


def fib(num):
    fib_list = [0, 1]
    for i in range(num - 2):
        fib_list.append(fib_list[i] + fib_list[i + 1])

    return fib_list


def post_list(request):
    #html = ', '.join(str(x) for x in fib(8))
    #html = 1/3
    #return HttpResponse(html)
    return render(request, 'blog/post_list.html', {})

    #   now = datetime.datetime.now()
    #   html = "<html><body>It is now %s.</body></html>" % now
    #   return HttpResponse(html)