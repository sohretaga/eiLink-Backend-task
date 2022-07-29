from django.contrib import admin
from .models import News
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = "News Task Administration"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "upvotes")
    list_filter = ("upvotes", "creation_date")
    search_fields = ("title",)

    admin.site.unregister(Group)
