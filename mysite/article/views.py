from django.shortcuts import render
from article.models import Article

# Create your views here.


def article(request):
    '''
    Render the article page
    '''
    articles = Article.objects.all()
    # 取出所有的文章，Django 稱查詢出來的資料為查詢集(Query set)
    context = {'articles': articles}
    # 利用範本變數article將查詢集至範本，修改範本以顯示文章資料在context區塊加到內容
    return render(request, 'article/article.html', context)
