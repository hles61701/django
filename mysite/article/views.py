from django.shortcuts import render
from article.models import Article, Comment
from article.forms import ArticleForm

# Create your views here.


def article(request):
    '''
    Render the article page
    '''

    # articles = Article.objects.all()
    # 取出所有的文章，Django 稱查詢出來的資料為查詢集(Query set)

    articles = {article: Comment.objects.filter(
        Article=article) for article in Article.objects.all()}
    # 將articles 變數改為一個dict K:V=文章:留言
    context = {'articles': articles}
    # 利用範本變數article將查詢集至範本，修改範本以顯示文章資料在context區塊加到內容
    return render(request, 'article/article.html', context)


def articleCreate(request):
    '''
    Create a new article instance
        1. If method is GET, render an empty form
        2. If method is POST,
            * vaildate the form and display error message if the form is invalid
            * else , save it to the model and redirect to the article page
    '''

    # # TODO: finish the code
    # return render(request, 'article/article.html') # 測試

    template = 'article/articleCreate.html'
    if request.method == 'GET':
        # print(ArticleForm()) 可以看到表單預設結構是table
        return render(request, template, {'articleForm': ArticleForm()})

    # POST
    articleForm = ArticleForm(request.POST)
    print(request.POST)
    # 如果驗證錯誤
    if not articleForm.is_valid():
        return render(request, template, {'articleForm': articleForm})

    articleForm.save()
    return article(request)
