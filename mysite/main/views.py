from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 測試01
# def main(request):
#     return HttpResponse('Hello Word')


def main(request):
    '''
    render the main page(呈現主業)
    '''
    html = '''
    <!doctype html>
    <html>
    <head>
    <title>部落格</title>
    <meta charset='utf-8'>
    </head>
    <body>
    <p>這是HTML版的HELLO WORD</p>
    </body>
    </hteml>
    '''
    return HttpResponse(html)
