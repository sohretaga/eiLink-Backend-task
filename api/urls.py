from django.urls import path
from . import views as api_views

urlpatterns = [
  path('news/', api_views.news_list_create_api_view, name='news-list'),
  path('news/<int:pk>/', api_views.news_detail_api_view, name='news-detail'),
]