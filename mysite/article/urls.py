from django.urls import path
from article import views

app_name = 'article'
urlpatterns = [
    path('', views.article, name='article'),
    path('articleCreate/', views.articleCreate, name='articleCreate'),
    path('articleRead/<int:articleId>/', views.articleRead, name='articleRead'),
    # <int:articleId> => URL中傳遞資料 int整數:articleId參數名稱

    path('articleUpdate/<int:articleId>/',
         views.articleUpdate, name='articleUpdate'),


]
