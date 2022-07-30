from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    link = models.URLField()
    upvotes = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "news"
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    news = models.ForeignKey(News, on_delete=models.CASCADE, blank=False, null=False, related_name='comments')
    content = models.TextField(max_length=500, blank=False, null=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comments"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self) -> str:
        return self.author.first_name
