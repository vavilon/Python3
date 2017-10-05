from django.shortcuts import render

# Create your views here.
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Lunch

# Create your views here.

class LunchForm(forms.Form):
    """Form object. Looks a lot like the WTForms Flask example"""
    submitter = forms.CharField(label='Your name')
    food = forms.CharField(label='What did you eat?')
