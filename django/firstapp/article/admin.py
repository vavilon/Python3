#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mptt.admin import MPTTModelAdmin
from django.contrib import admin
from article.models import Article, Comments,Home
from article.models import  Category,Keywords,Author

# Register your models here.
class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 1
class HomeAdmin(admin.ModelAdmin):

    fields =  ['home_title', 'home_text', 'home_date','home_image','video']
    list_display= ('home_title','home_date','home_image','bit_home')



class ArticleAdmin(admin.ModelAdmin):

    fields =  ['article_title', 'article_text','article_text_min','author', 'article_date','article_image','video','category','keywords']
    list_display= ('article_title','author','article_date','article_image','bit','category',)
    inlines = [ArticleInline]
    list_filter = ('category',)
    search_fields = ['article_title']

class CategoryAdmin(admin.ModelAdmin):
    fields =  ['name', 'parent']

class KeywordsAdmin(admin.ModelAdmin):
    fields =  ['name']

class AuthorAdmin(admin.ModelAdmin):

    fields =  ['name','author_image']
    list_display= ['name','author_image','bit_author']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Keywords,KeywordsAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Home,HomeAdmin)