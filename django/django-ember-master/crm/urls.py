from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from web import views

router = routers.DefaultRouter()
router.register(r'registration', views.RegistrationViewSet, base_name='registration')

urlpatterns = [
	url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
