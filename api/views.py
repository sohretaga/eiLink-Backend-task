from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from news.models import News, Comment
from api.serializers import NewsSerializer, CommentSerializer, UserSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class CommentListCreateAPIView(generics.ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



# News Model API
@api_view(["GET", "POST"])
def news_list_create_api_view(request):
    if request.method == "GET":
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def news_detail_api_view(request, pk):
    try:
        news = News.objects.get(pk=pk)

    except News.DoesNotExist:
        return Response(
            {"field": {"error": 404, "message": f"No news with id {pk} found"}},
            status=status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Comment Model API


# @api_view(["GET", "POST"])
# def comment_list_create_api_view(request):
#     if request.method == "GET":
#         comment = Comment.objects.all()
#         serializer = CommentSerializer(comment, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def comment_detail_api_view(request, pk):
#     try:
#         comment = Comment.objects.get(pk=pk)

#     except Comment.DoesNotExist:
#         return Response(
#             {"field": {"error": 404, "message": f"No comment with id {pk} found"}},
#             status=status.HTTP_404_NOT_FOUND,
#         )

#     if request.method == 'GET':
#         serializer = CommentSerializer(comment)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CommentSerializer(comment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)