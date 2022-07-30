from django.contrib import admin
from .models import News, Comment
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = "News Task Administration"
admin.site.unregister(Group)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "upvotes")
    list_filter = ("upvotes", "creation_date")
    search_fields = ("title",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'news', 'creation_date')
    list_filter = ( 'creation_date',)
    search_fields = ('author',)