#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template # отвечает за получение шаблона
from django.template import Context # овечает за хранение переменных, которые потом будут отправлены в шаблон
from django.shortcuts import render_to_response, redirect #
from article.models import Article, Comments,Category,Keywords,Author,Home  #
from django.core.exceptions import ObjectDoesNotExist #
from forms import CommentForm, KeywordsForm #
from django.core.context_processors import csrf #
from django.core.paginator import Paginator #
from django.contrib import auth #
from django.template import loader, Context, RequestContext
from django.http import HttpResponseRedirect #
from django.shortcuts import render #
import operator

from django.db import models
# Create your views here.






def articles(request, page_number=1):
    keywords_form = KeywordsForm
    args = {}
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 2)
    args['articles']= current_page.page(page_number)
    args['keywords'] = Keywords.objects.all()
    args['projects']=Category.objects.all()
    args['username'] = auth.get_user(request).username
    args['authors'] = Author.objects.all()
    args['form_keywords'] = keywords_form
    return render_to_response('articles.html',args)

def article(request, article_id=1):
    comment_form = CommentForm
    keywords_form = KeywordsForm
    args = {}
    args.update(csrf(request))
    args['projects']=Category.objects.all()
    args['article'] = Article.objects.get(id=article_id)
    args['category'] = Category.objects.filter(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['n_comments'] =args['comments'] .count()
    args['form'] = comment_form
    args['keywords'] = Keywords.objects.all()
    args['username'] = auth.get_user(request).username
    args['authors'] = Author.objects.all()
    args['form_keywords'] = keywords_form
    return render_to_response('article.html', args)

def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
            return_path = request.META.get('HTTP_REFERER','/')
            return redirect(return_path)
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            return_path = request.META.get('HTTP_REFERER','/')

            response = redirect(return_path)
            response.set_cookie( article_id,"test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')





def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():

            comment = form.save(commit=False)
            comment.comments_author = request.user
            comment.comments_article = Article.objects.get(id=article_id)


            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id)

def articl_cat(request, category_id=1):
    keywords_form = KeywordsForm
    args = {}
    args['projects']=Category.objects.all()
    args['category'] = Category.objects.get(id=category_id)
    args['articles'] = Article.objects.filter(category_id=category_id)
    args['username'] = auth.get_user(request).username
    args['authors'] = Author.objects.all()
    branch_categories = args['category'].get_descendants(include_self=True)
    args['category_articles'] =Article .objects.filter(category__in=branch_categories).distinct()
    args['keywords'] = Keywords.objects.all()
    args['form_keywords'] = keywords_form
    return render_to_response('articl_cat.html', args)

def keywords (request): #
# Выберем все articles, которые имеют выбранный тег
    keywords_form = KeywordsForm
    return_path = request.META.get('HTTP_REFERER','/')
    args = {}
    args['authors'] = Author.objects.all()
    args['keywords'] = Keywords.objects.all()
    args['projects']=Category.objects.all()
    args['username'] = auth.get_user(request).username
    args['form_keywords'] = keywords_form
    args.update(csrf(request))
    if request.POST:
        key = request.POST.get('name', '')
        args['key_name']= key
        args['articles'] = Article.objects.filter(keywords__name__exact=key)
        if args['articles']:

             return render_to_response('keywpage.html',args )
        else:

             return render_to_response('keywpage_no.html',args )
    else:
        return redirect(return_path)

def authors (request, id): #
# Выберем все articles, которые имеют выбранный author

    keywords_form = KeywordsForm
    args = {}
    args['form_keywords'] = keywords_form
    args['authors'] = Author.objects.all()
    args['author_s'] =Author.objects.get(id=id)
    args['articles'] = Article.objects.filter(author__name__exact=args['author_s'])
    args['projects']=Category.objects.all()
    args['username'] = auth.get_user(request).username
    return render(request, 'author_page.html', args)

def home(request):
    keywords_form = KeywordsForm
    args = {}
    args['articles']=Article.objects.all()
    args['authors'] = Author.objects.all()
    args['projects']=Category.objects.all()
    args['username'] = auth.get_user(request).username
    args['homes']= Home.objects.all()
    args['form_keywords'] = keywords_form
    return render(request, 'home.html', args)