# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf


def search_post(request):
    """
    用于接收post请求
    """
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, 'post.html', ctx)

