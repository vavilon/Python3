from django.contrib import admin

# Register your models here.
#from django.contrib import admin

from .models import Section, Article

admin.site.register(Section)
admin.site.register(Article)
