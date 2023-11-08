from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from common.models import Customer


def listorders(request):
    return HttpResponse("下面是订单系统的全部信息。。。")

def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()

    #检查URL中是否存在参数phonenumber
    ph = request.GET.get('phonenumber',None)

    #如果有，添加过滤条件
    if ph:
        qs = qs.filter(phonenumber=ph)

    #定义返回字符串
    retStr = ''
    for customer in qs:
        for name , value  in customer.items():
            retStr += f'{name} : {value} | '
            #<br>表示换行
        retStr += '<br>'

    return HttpResponse(retStr)
