from django.db import models

# Create your models here.
#from django.db import models
from django.contrib.auth.models import User

Class UserProfil(models.Model):
    user = models.OneToOneField(User,verbose_name='User', related_name='profile')
    address = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    login_count = models.PositiveIntegerField(default=0)
