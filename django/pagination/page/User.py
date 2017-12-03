from django.contrib.auth.models import User
from django.core.paginator import Paginator

user_list = User.objects.all()
paginator = Paginator(user_list, 10)
