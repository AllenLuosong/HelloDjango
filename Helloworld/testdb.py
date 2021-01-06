# -*- coding: utf-8 -*-

from django.http import HttpResponse
from TestModel.models import Test


# 数据库操作
def testdb(request):
    # 初始化
    response = ''
    response1 = ''
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()
    # filter 设置过滤条件，相当于where
    response2 = Test.objects.get(id=2)
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    response2.name = 'Google'
    response2.save()
    # 另一种修改方式
    Test.objects.filter(id=3).update(name='Baidu')
    # 获取单个对象
    # response3 = Test.objects.get(id=1)

    for vars in list:
        response1 += vars.name + ""
    response = response1
    # test1 = Test(name="runoob")
    # test1.save()
    return HttpResponse("<p>" + response + " " + "</p>")
