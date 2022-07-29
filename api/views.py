from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from news.models import News
from api.serializers import NewsSerializer


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
