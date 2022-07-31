from rest_framework import serializers
from news.models import News, Comment
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Comment
        exclude = ("news",)


class NewsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = "__all__"
