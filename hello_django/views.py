from django.shortcuts import render, HttpResponse

def say_hello(requst):
    return HttpResponse("Hello Django!")