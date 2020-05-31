from django.urls import path
from article.views import article_list, article_content, article_comment

urlpatterns = [
    path('articles/', article_list),
    path('articles/<int:id>/',article_content),
    path('articles/<int:id>/comments',article_comment)
]