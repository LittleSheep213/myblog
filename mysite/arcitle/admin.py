from django.contrib import admin
from . models import Article

# Register your models here.
@admin.register(Article)
# 自定义Article的控制台界面
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "author", "content", "create_time", "last_update_time", "is_deleted", "read_num")
	ordering = ("id",)
# 就是让你能在管理员界面看到Article类
# admin.site.register(Article, ArticleAdmin)