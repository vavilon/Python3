# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})
