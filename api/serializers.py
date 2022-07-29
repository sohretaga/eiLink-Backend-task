from rest_framework import serializers
from news.models import News
from datetime import datetime, date
from django.utils import timesince


class NewsSerializer(serializers.ModelSerializer):
    # time_since_publish = serializers.SerializerMethodField()

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
