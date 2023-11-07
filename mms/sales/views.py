from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def listorders(request):
    return HttpResponse("下面是订单系统的全部信息。。。")