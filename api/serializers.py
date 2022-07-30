from rest_framework import serializers
from news.models import News, Comment
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


# from datetime import datetime, date
# from django.utils import timesince


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    # validate_password = make_password



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    # time_since_publish = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = "__all__"
        # fields = ('title', 'author', 'link', 'upvotes', 'creation_date')
        # exclude = ('upvotes')

    # def get_time_since_publish(self, object):
    #     now = datetime.now()
    #     publish_date = object.creation_date
    #     since = timesince(publish_date, now)
    #     return since

    # def validate_creation_date(self, timevalue):
    #     if timevalue > date.today():
    #         raise serializers.ValidationError("Publish date cannot be a future date!")
    #     return timevalue
