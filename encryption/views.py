# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import os


# Create your views here.


def encryptionMain(request):
    print("encryptionMain")
    return render(request,"enc/encIndex.html")
    return HttpResponse("This is in encryption application!")

def testGet(request,num):
    #注意，这里的参数num是一个字符串
    return HttpResponse("input number is %s"%(num))