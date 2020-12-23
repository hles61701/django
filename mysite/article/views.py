from django.shortcuts import render, redirect, get_object_or_404
from article.models import Article, Comment
from article.forms import ArticleForm
from django.contrib import messages

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

    template = 'article/articleCreateUpdate.html'
    if request.method == 'GET':
        # print(ArticleForm()) 可以看到表單預設結構是table
        return render(request, template, {'articleForm': ArticleForm()})

    # POST
    articleForm = ArticleForm(request.POST)

    # 如果驗證錯誤
    if not articleForm.is_valid():
        return render(request, template, {'articleForm': articleForm})

    articleForm.save()
    # return article(request)
    messages.success(request, '文章已新增')
    return redirect('article:article')  # 轉向到article


def articleRead(request, articleId):
    '''
    Read an article
        1. Get the article instance; redirect to the 404 page if not found
        2. Render the articleRead template with the article instance and its associated comments
    '''
    article = get_object_or_404(Article, id=articleId)
    context = {
        'article': article,
        # 'comments': Comment.objects.filter(article=article)
        'comments': Comment.objects.filter(Article=article)
    }
    return render(request, 'article/articleRead.html', context)


def articleUpdate(request, articleId):
    '''
    Update the article instance:
        1. Get the article to update; redirect to 404 if not found
        2. If method is GET, render a bound form
        3. If method is POST,
            * vaildate the form and render a bound form if the form is invalid
            * else, save it to the model and redirect to the article page
    '''
    # # TODO: finish the code
    # return render(request, 'article/article.html') 測試
    article = get_object_or_404(Article, id=articleId)
    template = 'article/articleCreateUpdate.html'
    if request.method == 'GET':
        articleForm = ArticleForm(instance=article)
        return render(request, template, {'articleForm': articleForm})

    # POST
    articleForm = ArticleForm(request.POST, instance=article)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm': articleForm})

    articleForm.save()
    messages.success(request, '文章已修改')
    return redirect('article:articleRead', articleId=articleId)


def articleDelete(request, articleId):
    '''
    '''
    if request == 'GET':
        return render('article:article')

    # POST
    article = get_object_or_404(Article, id=articleId)
    article.delete()
    messages.success(request, '文章已刪除')
    return redirect('article:article')
