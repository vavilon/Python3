#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.forms import ModelForm
from models import Comments,Keywords

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']

class KeywordsForm(ModelForm):
    class Meta:
        model = Keywords
        fields = ['name']