from django.contrib import admin

from .models import Registration

class RegistrationAdmin(admin.ModelAdmin):
	list_display = ('id', 'firstname', 'lastname')

admin.site.register(Registration, RegistrationAdmin)
