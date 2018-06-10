from django.contrib import admin
from .models import Article, Comment

# Register your models here.


@admin.register(Article, Comment) #model.py의 comment 함수
class BlogAdmin(admin.ModelAdmin):
    pass
