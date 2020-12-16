from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

# 測試01
# def main(request):
#     return HttpResponse('Hello Word')

# 測試02
# def main(request):
#     '''
#     render the main page(呈現主頁)
#     '''
#     html = '''
#     <!doctype html>
#     <html>
#     <head>
#     <title>部落格</title>
#     <meta charset='utf-8'>
#     </head>
#     <body>
#     <p>這是HTML版的HELLO WORD</p>
#     </body>
#     </hteml>
#     '''
#     return HttpResponse(html)


def main(request):
    '''
    render the main page
    '''
    context = {'like': 'Django 很棒喔'}
    return render(request, 'main/main.html', context)




def about(request):
    '''
    render the main page
    '''
    return render(request, 'main/about.html')


