from django.urls import path
from . import views as api_views

urlpatterns = [
    path("users/", api_views.UserListCreateAPIView.as_view(), name="user-list"),
    path("user/<int:pk>/", api_views.UserDetailAPIView.as_view(), name="user-detail"),

    path("news/", api_views.news_list_create_api_view, name="news-list"),
    path("news/<int:pk>/", api_views.news_detail_api_view, name="news-detail"),
    path('news/<int:news_pk>/add-comment/', api_views.CommentCreateAPIView.as_view(), name="add-comment"),

    path('comments/', api_views.CommentListCreateAPIView.as_view(), name="comment-list"),
    path('comment/<int:pk>/', api_views.CommentDetailAPIView.as_view(), name="comment-detail"),

    path('upvote/<int:pk>/add-upvote/', api_views.news_upvote_update, name="add-upvote"),
] 
