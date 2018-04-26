# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import os


# Create your views here.


def ForWSMain(request):
    return HttpResponse("This is in ForWinService application!")
