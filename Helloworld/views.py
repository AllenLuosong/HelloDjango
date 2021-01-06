from django.http import HttpResponse
from django.shortcuts import render


def runoob(request):
    """
    新增一个对象，用于向模板提交数据
    使用 render 来替代之前使用的 HttpResponse。render 还使用了一个字典 context 作为参数。
    context 字典中元素的键值 hello 对应了模板中的变量 {{ hello }}。
    """
    import datetime
    view_list = ["菜鸟教程", "菜鸟教程1", "菜鸟教程2", "菜鸟教程3", ]
    view_str = "菜鸟教程"
    view_dict = {"name": "菜鸟教程", "age": "18"}
    # name = 0  # 如果view值传的变量布尔类型为false时则使用指定默认值 0为fasle
    now = datetime.datetime.now()
    name = '菜鸟教程123456'
    view_num = 88
    context = {"name": name, 'time': now, 'view_str': view_str, "num": view_num, "view_list": view_list,
               "view_dict": view_dict}

    return render(request, 'runoob.html', context)


def hello(request):
    hello = [1, 2, 3]
    context = {'view_list': hello}
    return render(request, 'runoob.html', context)

    # return HttpResponse("Hello world ! ")
