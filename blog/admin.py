from django.contrib import admin
from blog.models import Commentary, User, Post
from django.contrib.auth.models import Group


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "content", "owner__username")
    list_filter = ("created_time", "owner")
    ordering = ("-created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "content", "created_time")
    search_fields = ("content", "user__username", "post__title")
    list_filter = ("created_time",)
    ordering = ("-created_time",)


admin.site.register(User)
admin.site.unregister(Group)
