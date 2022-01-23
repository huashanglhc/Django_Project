# -*- coding: utf-8 -*-
# @Author: wl
# @File  : views.py
# @Date  : 2022/1/8 21:56
# @Desc  :

from django.http import HttpResponse


def index(request):

    html = "<h1>hello django<h1>"

    return HttpResponse(html)


def test_request(request):
    print("test_request...", request)
    print("test_request...", request.__dict__)
    print("test_request...", dir(request))
    print("request.path", request.path)

    return HttpResponse("hello world")