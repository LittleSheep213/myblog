from django.urls import path
from .views import article_detail, article_list
urlpatterns = [
    path('<article_id>', article_detail, name='article_detail'),
    path('', article_list, name='article_list'),
]
