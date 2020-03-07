from django.shortcuts import render
from django.http import HttpResponse


def give_otp(req):
    return HttpResponse('<h1>Hello World</h1>')
