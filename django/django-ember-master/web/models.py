from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError

class Registration(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('unspecified', 'Unspecified')
    )

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    # gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    # email = models.EmailField(max_length=100)

    # newsletter = models.BooleanField(default=False, help_text='Subscribed to email list')
    # magazine = models.BooleanField(default=False, help_text='Receives print magazine')
    # promotions = models.BooleanField(default=False, help_text='Opted into receiving promotions')

    submitted = models.DateTimeField(auto_now_add=True)
    