from django.contrib import admin
from . models import Article

# Register your models here.就是让你能在管理员界面看到Article类
admin.site.register(Article)