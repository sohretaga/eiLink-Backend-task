from django.urls import path
from . import views as api_views

urlpatterns = [
    path("users/", api_views.UserListCreateAPIView.as_view(), name="user-list"),
    path("user/<int:pk>/", api_views.UserDetailAPIView.as_view(), name="user-detail"),

    path("news/", api_views.news_list_create_api_view, name="news-list"),
    path("news/<int:pk>/", api_views.news_detail_api_view, name="news-detail"),

    path('comments/', api_views.CommentListCreateAPIView.as_view(), name="comment-list"),
    path('comment/<int:pk>/', api_views.CommentDetailAPIView.as_view(), name="comment-detail"),
]
